from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """主页 - 显示所有博客文章"""
    posts = BlogPost.objects.all().order_by('-date_added')
    
    is_authenticated = request.user.is_authenticated
    
    user_post_count = 0
    if is_authenticated:
        user_post_count = BlogPost.objects.filter(owner=request.user).count()
    
    context = {
        'posts': posts,
        'is_authenticated': is_authenticated,
        'user_post_count': user_post_count,
    }
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """添加新博客文章"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')
    
    context = {'form': form, 'page_title': '发布新文章'}
    return render(request, 'blogs/post_form.html', context)

@login_required
def edit_post(request, post_id):
    """编辑现有博客文章"""
    post = get_object_or_404(BlogPost, id=post_id)
    
    # 🔒 关键权限控制：检查用户是否是文章所有者
    if post.owner != request.user:
        return HttpResponseForbidden("❌ 您无权编辑此文章。")
    
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    
    context = {
        'form': form,
        'post': post,
        'page_title': f'编辑文章: {post.title}'
    }
    return render(request, 'blogs/post_form.html', context)

def user_posts(request, username):
    """显示特定用户的所有文章"""
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(owner=user).order_by('-date_added')
    
    context = {
        'posts': posts,
        'page_title': f'{user.username} 的文章',
        'target_user': user,
    }
    return render(request, 'blogs/index.html', context)