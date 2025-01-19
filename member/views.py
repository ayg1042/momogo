from django.shortcuts import render

# Create your views here.
def signup_page(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')