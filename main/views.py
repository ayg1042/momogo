from django.shortcuts import render
# from .models import Post

# Create your views here.
def index(request):
    return render(request,'index.html')

# # 게시판 테스트
# def blog(request):
#     # 모든 post를 가져와 postlist에 저장합니다.
#     postlist = Post.objects.all()

#     return render(request, 'subPage/blog.html', {'postlist':postlist})

# # blog의 게시글(posting)을 부르는 posting 함수
# def posting(request, pk):
#     # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
#     post = Post.objects.get(pk=pk)
#     # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
#     return render(request, 'subPage/posting.html', {'post':post})