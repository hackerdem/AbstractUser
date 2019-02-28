from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView
from .models import MyUser

class CreateUserView(CreateView):
    model = MyUser
    fields = ['email', 'password', 'first_name', 'bio', 'location', 'relocation']
    success_url = 'create-done'

class DetailUserView(DetailView):
    model = MyUser

class CreateDoneTemplateView(TemplateView):
    template_name = 'create-done.html'