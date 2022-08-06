from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='user-login')
def home(request):
    # tasks = Task.objects.filter(user=request.user)
    posts = request.user.posts.all()
    return render(request, "posts/home.html", {"posts": posts})


@login_required(login_url='user-login')
def create_post(request):
    pass