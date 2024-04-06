import os
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
     print(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
     return render(request, 'index.html')
