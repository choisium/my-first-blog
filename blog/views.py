from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	return render(request, 'blog/post_list.html', {})


def post_list(request):
    # 글 목록을 게시일 published_date 기준으로 정렬
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 글 목록을 템플릿에 딕셔너리 형태로 전달함
    return render(request, 'blog/post_list.html', {'posts': posts})