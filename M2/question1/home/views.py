from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from .forms import SignupForm, toDoForm
from django.contrib import messages
from .models import toDo

# Create your views here.
def home(request):
    return render(request, "home.html")

def dashboard(request):
    data=toDo.objects.all()
    context={"data":data}
    return render(request, 'dashboard.html', context)

def toDoAdd(request):
    form=toDoForm()
    if request.method=="POST":
        data=toDoForm(request.POST)
        if data.is_valid():
            data.save()

            #print message success
            messages.success(request, "To-Do Added Successfully")
            return redirect('dashboard')
        else:
            #print failure message
            return redirect('dashboard')
    context={"form":form}
    return render(request, 'crud/toDoAdd.html', context)

def toDoUpdate(request, id):
    data=toDo.objects.get(id=id)
    update_todo=toDoForm(request.POST or None, instance=data)
    if update_todo.is_valid():
        update_todo.save()

        #print message success
        messages.success(request, "To-Do Updated Successfully")
        return redirect('dashboard')
    context={"form":update_todo}
    return render(request, 'crud/toDoUpdate.html', context)

def toDoDelete(request, id):
    data=toDo.objects.get(id=id)
    data.delete()
    #print success message
    messages.success(request, "To-Do Deleted Successfully")
    return redirect('dashboard')

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        passw=request.POST['passw']
        user=authenticate(request, username=username, password=passw)
        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            return redirect("login")
    else:
        return render(request, "auth_user/login.html")

def logout_user(request):
    logout(request)
    return redirect('home')

def signup_user(request):
    if request.method=="POST":
        data=SignupForm(request.POST)
        if data.is_valid():
            new_user=data.save()

            login(request, new_user)
            return redirect('home')
    else:
        data=SignupForm()

    return render(request, "auth_user/signup.html", {"form":data})