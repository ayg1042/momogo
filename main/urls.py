from django.urls import path
from . import views

app_name = ''


urlpatterns = [
    path('', views.index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    # path('blog/', views.blog, name='blog'),
    # # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    # path('blog/<int:pk>/', views.posting, name="posting"),
]