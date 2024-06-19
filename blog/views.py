from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Post, Comment, Like, Follow
from authorization.models import MyUser


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    myuser = MyUser.objects.filter(user=request.user).first()
    follow_obj = Follow.objects.all()
    me_followed_users = [user.following for user in follow_obj]

    if request.method == 'POST':
        image = request.FILES.get('image')
        print(image)
        if image:
            obj = Post.objects.create(user=myuser, image=image)
            obj.save()
            return redirect('home')

    like = Like.objects.all()

    posts = Post.objects.all().exclude(user=myuser)
    me_posts = []
    for post in posts:
        for me_followed_user in me_followed_users:
            if post.user == me_followed_user:
                me_posts.append(post)

    for post in me_posts:
        post.like_count = like.filter(post_id=post.id).count()

    comments = Comment.objects.all()

    myusers = list(MyUser.objects.all().exclude(user=request.user))
    objects = follow_obj.filter(follower=myuser)
    for obj in objects:
        if obj.following in myusers:
            myusers.remove(obj.following)
    for user in myusers:
        user.following_count = follow_obj.filter(following_id=user.id, follower=myuser).count()

    return render(request, 'index.html', {'posts': me_posts,
                                          'comments': comments,
                                          'myuser': myuser,
                                          'users': myusers})


def search_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    text = request.GET.get('q')
    text = text.lower()
    print(text)
    if text:
        user = MyUser.objects.filter(user__username=text).first()
        if user:
            return redirect(f'/profile/{user.id}')
    return redirect('home')


def post_comment_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    myuser = MyUser.objects.filter(user=request.user).first()
    text = request.GET.get('text')
    id = request.GET.get('id')
    if len(text) > 0:
        pk = request.GET.get('id')
        obj = Comment.objects.create(user=myuser, text=text, post_id=pk)
        obj.save()
    return redirect(f'/#{id}')


def profile_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    myuser = MyUser.objects.filter(id=pk).first()
    posts = Post.objects.filter(user__id=myuser.id)
    followers = len(Follow.objects.filter(following=myuser))
    following = len(Follow.objects.filter(follower=myuser))
    return render(request, 'profile.html', {'myuser': myuser,
                                            'posts': posts,
                                            'followers': followers,
                                            'following': following})


def like_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    myuser = MyUser.objects.filter(id=pk).first()
    if Like.objects.filter(user=myuser, post_id=pk).exists():
        Like.objects.filter(user=myuser, post_id=pk).delete()
        return redirect(f'/#{pk}')
    obj = Like.objects.create(user=myuser, post_id=pk)
    obj.save()
    return redirect(f'/#{pk}')


def accaunt_settings_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    message = {}
    myuser = MyUser.objects.filter(user=request.user).first()
    if request.method == 'POST':
        image = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        print(image)
        print(first_name)
        if image:
            myuser.image = image
            myuser.save()
        if first_name:
            request.user.first_name = first_name
            request.user.save()
        if username:
            if not User.objects.filter(username=username).exists():
                request.user.username = username
                request.save()
            else:
                message = {'message': 'Username already taken'}
        return redirect('/accaunt')
    return render(request, 'account-setting.html', {"myuser": myuser, 'message': message})


def follow(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    next = request.GET.get('next')
    myuser = MyUser.objects.filter(user=request.user).first()
    if not Follow.objects.filter(follower=myuser, following_id=pk).exists():
        obj = Follow.objects.create(follower=myuser, following_id=pk)
        obj.save()
        return redirect(f'{next}')
    Follow.objects.filter(follower=myuser, following_id=pk).delete()
    return redirect(f'{next}')