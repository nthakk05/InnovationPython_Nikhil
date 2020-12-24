from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Blog

class BlogList(ListView):
    model = Blog

class BlogView(DetailView):
    model = Blog

class BlogCreate(CreateView):
    model = Blog
    fields = ['AuthorName', 'Title','Content']
    success_url = reverse_lazy('blog_list')

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['AuthorName', 'Title','Content']
    success_url = reverse_lazy('blog_list')

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')