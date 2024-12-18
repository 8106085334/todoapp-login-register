#from django.http import HttpResponse
from django.shortcuts import render,redirect
from todos.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def homepage(request):
    return render(request,'homepage.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            # Get the username from the form
            username = form.cleaned_data.get('username')

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username is already taken. Please choose a different one.")
                return redirect('register')  # Redirect back to the registration page

            # If the username doesn't exist, save the user
            form.save()
            messages.success(request, f"Hi {username}, Your account has been created successfully! Please log in.")
            return redirect('login')  # You can change this to wherever you want to redirect after successful registration

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user) 
            return redirect('home')
    # A backend authenticated the credentials

        else:
            messages.error(request, "Invalid username or password")
            return render(request,'login.html')
    # No backend authenticated the credentials
    return render(request,'login.html')

        
    

def logoutUser(request):
    logout()
    return redirect('login')

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completed_task = Task.objects.filter(is_completed=True)

    context = {
        'tasks':tasks,
        'completed_task':completed_task,
    }

    return render(request,'index.html',context)