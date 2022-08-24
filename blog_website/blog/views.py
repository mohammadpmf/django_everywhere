from django.shortcuts import redirect, render, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm

def post_list_view(request):
    # posts_list = Post.objects.all() # Hama ro migire.
    posts_list = Post.objects.filter(status='pub').order_by('-date_modified')
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


# Raveshe 1
# def post_create_view(request):
#     # print(request.method)
#     if request.method == 'POST':
#         print(request.POST)
#         post_title = request.POST.get('title')
#         post_text = request.POST.get('text')
#         Post.objects.create(title=post_title, text=post_text, author=User.objects.all()[0], status='pub')
#     elif request.method == 'GET':
#         print("GET request.")
#     return render(request, 'blog/post_create.html')

# Raveshe 2
def post_create_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
            
    else:
        form = NewPostForm()
    return render (request, 'blog/post_create.html', context={'form': form})

def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts_list')
    return render(request, 'blog/post_create.html', context={'form': form})

def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')
    return render(request, 'blog/post_delete.html', context={'post': post})
