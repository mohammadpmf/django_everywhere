from django.shortcuts import render
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

def post_list_view(request):
    # posts_list = Post.objects.all() # Hama ro migire.
    posts_list = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

def post_detail_view(request, pk):
    # Raveshe 1
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     post = None
    # return render(request, 'blog/post_detail.html', {'post': post})

    # Raveshe 2
    # try:
    #     post = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:
    #     post = None
    # return render(request, 'blog/post_detail.html', {'post': post})

    # Raveshe 3
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})