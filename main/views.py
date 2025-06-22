from django.shortcuts import render
# from .models import Post

# Create your views here.
def index(request):
    user_id = request.session.get('user_id')
    return render(request,'index.html', {'user_id': user_id})