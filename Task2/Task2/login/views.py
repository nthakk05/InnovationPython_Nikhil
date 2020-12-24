
from django.http import HttpResponse
from django.shortcuts import render
from django import forms
# Create your views here.

def Home(request):
    return render(request, "Home.html")

def Congratulations (request):
    return render(request, "login/Congratulations.html")

class LoginForm(forms.Form):
    UserName = forms.CharField(label="Username", max_length=30, required=True)
    EmailAddress = forms.EmailField(label="EmailAddress", max_length = 200, required=True)
    password = forms.CharField(label="Password", max_length=50, required=True)

def save_form(request):
    form1 = LoginForm(request.POST or None)
    """if form1.is_valid():
        form1.save()
        form1 = LoginForm()"""
    context = {'Nik1': form1}
    return render(request,"login/index.html", context)

"""<a href="{% url 'Home' %}"> Home </a>"""

"""    {{ form.as_p }}"""

