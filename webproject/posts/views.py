from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from posts.forms import PostsModelForm
from posts.models import Post


@login_required(login_url='user-login')
def home(request):
    # tasks = Task.objects.filter(user=request.user)
    posts = Post.objects.all()
    # posts = get_object_or_404(Post)
    return render(request, "posts/home.html", {"posts": posts})


@login_required(login_url='user-login')
def user_posts(request):
    # tasks = Task.objects.filter(user=request.user)
    posts = request.user.posts.all()
    return render(request, "posts/home.html", {"posts": posts})


@login_required(login_url='user-login')
def create_post(request):
    # form = PostsModelForm()
    if request.method == "POST":
        form = PostsModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('homepage')

        return render(request, 'posts/profile.html', {'form': form})
    else:
        form = PostsModelForm()
        return render(request, 'posts/profile.html', {'form': form})
