from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# Create your views here.


def AboutUs(request):
    return render(request, "login2/AboutUs.html")

def index(request):
    context = {'user': request.user }
    return render(request, "login2/success.html", context)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('/success')

    else:
        form = AuthenticationForm()
    return render(request, 'login2/login2.html', {'login_c':form})


def logout (request):
    if request.method =='POST':
        logout(request)
        return redirect('login')