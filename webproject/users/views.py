from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import LoginForm, ProfileModelForm, UserRegisterForm
from users.models import Profile


# @login_required(login_url='user-login')
# def home(request):
#     # tasks = Task.objects.filter(user=request.user)
#     posts = request.user.posts.all()
#     return render(request, "tasks/home.html", {"tasks": posts, "count": posts.count()})


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.email = form.cleaned_data["email"]
            user.save()
            return redirect("user-login")

    return render(request, 'users/register.html', {'form': form})


def user_login(request):
    next_page = request.GET.get("next")
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)  # or user or None
            if user:
                login(request, user)
                # return HttpResponse('homepage')
                return redirect(next_page) if next_page else redirect('homepage')
            else:
                return HttpResponse("Wrong credentials!")

    return render(request, "users/login.html", {"form": form})


@login_required(login_url='user-login')
def user_logout(request):
    logout(request)
    return redirect("user-login")


@login_required(login_url='user-login')
def user_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    return render(request, "users/profile.html", context={"profile": profile})


@login_required(login_url='user-login')
def update_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileModelForm(instance=profile)
    if request.method == "POST":
        form = ProfileModelForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if request.FILES:
                profile.profile_image = request.FILES["profile_image"]
            profile.save()

            messages.success(request, "Profile is Updated")
            return redirect('user-profile')

    return render(request, "users/update_profile.html", context={"form": form})


