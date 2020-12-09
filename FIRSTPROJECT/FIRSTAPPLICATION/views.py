from django.shortcuts import render

from django.http import HttpResponse

#from .form import NameForm

def welcome(request):
    connecter = {'Nik':'"Nik'}
    return render(request, "index.html", connecter)

"""def get_name(request):
    form = NameForm()
    context = {'form': form}
    return  render(request,"index.html", context)
def Thnaks(request):
    return HttpResponse("Thank you for submit your information")
"""