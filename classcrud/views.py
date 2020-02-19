from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView # Show Data
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # Manage Data
from .models import ClassBlog


class BlogView(ListView):   # HTML Template : Blog Lists -> (소문자모델)_list.html
    model = ClassBlog

class BlogCreate(CreateView):   # HTML Template : Input Form for Create -> (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView):   # HTML Template : Detail Page -> (소문자모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView):   # HTML Template : Input Form for Update -> (소문자모델)_form. html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView):   # HTML Template : Confirm for Delete -> (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')