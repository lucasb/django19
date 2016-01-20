from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from waffle.decorators import waffle_flag

from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    post = get_object_or_404(Post, id=id)
    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'posts': posts, 'form': comment_form})

def add_comment_to_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', id=id)

@login_required
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

@login_required
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

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())\
                        .order_by('published_date')
    drafts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'drafts': drafts, 'posts': posts})

@login_required
def post_publish(request, id):
    post = get_object_or_404(Post, id=id)
    post.publish()
    return redirect('blog.views.post_detail', id=id)

@login_required
def post_delete(request, id=id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def comment_approve(request, id=id):
    comment = get_object_or_404(Comment, id=id)
    comment.approve()
    return redirect('blog.views.post_detail', id=comment.post.id)

@login_required
def comment_remove(request, id=id):
    comment = get_object_or_404(Comment, id=id)
    post_id = comment.post.id
    comment.delete()
    return redirect('blog.views.post_detail', id=post_id)

@waffle_flag('thrends')
def thrends_tags(request):
    return render(request, 'blog/thrends_tag.html', {'thrends': []})
