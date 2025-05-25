from django.shortcuts import render
from BapGo import models

# Create your views here.
def result(request):
    return render(request,'result.html')