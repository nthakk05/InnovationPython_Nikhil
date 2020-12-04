from django.shortcuts import render

from django.http import HttpResponse


def welcome(request):
    connecter = {'Nik':'"Nik'}
    return render(request, "index.html", connecter)