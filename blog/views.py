from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post, 'posts': posts})

def post_new(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'posts': posts})

def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'posts': posts})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    drafts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'drafts': drafts, 'posts': posts})

def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    post.publish()
    return redirect('blog.views.post_detail', id=id)
