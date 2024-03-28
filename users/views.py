from django.shortcuts import render, redirect, HttpResponse
from .models import ProjectUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        profile_picture = request.FILES.get('profile_picture', None)

        if name and email and password1 and password2:
            # Check if email already exists
            if ProjectUser.objects.filter(email=email).exists():
                print("User Alraedy Exists")
                return render(request, 'users/signup.html')
            
            
            user = ProjectUser.objects.create_user(name, email, password1)
            user.name = name
            if profile_picture:
                user.profile_picture = profile_picture
            
            user.save()
            print('User created:', user)

            return redirect('/login/')
        else:
            print('Something went wrong')
    else:
        print('Just show the form!')

    return render(request, 'users/signup.html')
            

def login_view(request):
    if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            username = ''
            try:
                username = ProjectUser.objects.get(email=email).username
            except ProjectUser.DoesNotExist:
                return HttpResponse("Invalid")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Logged in")
                return redirect('dashboard')
            else:
                print("not logged in")
            return redirect('signup')
    else:
        return render(request, 'users/login.html')

@login_required(login_url='/login/')
def dashboard_view(request):
    # The user is authenticated, render the dashboard
    return render(request, "users/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect('login')