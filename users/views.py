from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from django import forms

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, your account was created successfully")
            return redirect("ui:home")
    else:
        form = SignUpForm()
    
    return render(request, "users/register.html", {'form':form})



# def register_view(request):
#     form = SignUpForm()
#     if request.method == "POST":
        # form = SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     email=form.cleaned_data['username']
        #     password=form.cleaned_data['password1']
        #     user = authenticate(password=password, email=email)
        #     login(request, user)
        #     messages.success(request, ("You have been logged on"))
        #     return redirect('home')
        # else:
        #     messages.success(request, ("Whoops"))
        #     return redirect('users:register')
        # dave gray
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     login(request, form.save())
        #     return redirect("posts:list")
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         login(request, form.save())
    #         return redirect("posts:list")
    # else:
    #     # form = UserCreationForm()
    #     return render(request, "users/register.html", {'form':form})
    
    # return render(request, "users/register.html", {'form':form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in"))
            return redirect("ui:home")
        else:
            messages.error(request, ("There was an error"))
            return redirect('users:login')        
    
    return render(request, "users/login.html")
# def login_view(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if email is not None:
#             login(request, user)
#             messages.success(request, ("You have been logged in"))
#             return redirect("posts:list")
#         else:
#             messages.success(request, ("There was an error"))
#             return redirect('users:login')
        # form = AuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     login(request, form.get_user())
        #     return redirect("users:login")
    # else:
    #     form = AuthenticationForm()
    # return render(request, "users/login.html", {'form':form})
    

def logout_view(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect('ui:home')