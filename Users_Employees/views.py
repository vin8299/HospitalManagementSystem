from django.shortcuts import redirect, render, Http404
from django.contrib.auth import authenticate, login, logout
from .forms import UserLogin, UserRegistration


def SignUp(request):
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        password = form.cleaned_data.get("password")
        instance = form.save(commit=False)
        # encrypting the password
        instance.set_password(password)
        instance.save()
        return redirect("signin")

    context = {
                "title": "Sign Up",
                "form": form
              }
    return render(request, "signup.html", context)

def SignIn(request):
    if request.user.is_authenticated:
        raise Http404("Already login")
    form = UserLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(request, username=username,
                                     password=password)

        if user:
            
            login(request, user)
            return redirect("home")

    context = {
                "title": "Sign In",
                "form": form
              }
    return render(request, "signin.html", context)


def SignOut(request):
    logout(request)
    return redirect("signin")


