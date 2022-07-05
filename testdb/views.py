from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView

from .models import Student

class Add(CreateView):
    model = Student
    fields = ('name','age')
    template_name = 'add.html'
    success_url = '/testdb/'