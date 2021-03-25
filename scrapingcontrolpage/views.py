from django.shortcuts import render
from .models import papers

def home(request):
    paper = papers.objects.all()
    return render(request, 'home.html', {'papers': paper})