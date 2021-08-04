from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ListModel
from django.urls import reverse_lazy

# Create your views here.

class PostList(ListView):
    template_name = 'list.html'
    model = ListModel


class PostDetail(DetailView):
    template_name = 'detail.html'
    model = ListModel


class PostCreate(CreateView):
    template_name = 'create.html'
    model = ListModel
    fields = ('name','tel','units','company','bb','layaway','remarks')
    success_url = reverse_lazy('list')


class PostDelete(DeleteView):
    template_name = 'delete.html'
    model = ListModel
    success_url = reverse_lazy('list')


class PostUpdate(UpdateView):
    template_name = 'update.html'
    model = ListModel
    fields = ('name','tel','units','company','bb','layaway','remarks')
    success_url = reverse_lazy('list')
