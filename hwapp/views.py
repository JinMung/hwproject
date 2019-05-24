from django.shortcuts import render
from .models import Twice

def home(request):
    members=Twice.objects.filter(nationality='JP')
    return render(request,'home.html',{'japanese' : members})

# Create your views here.
