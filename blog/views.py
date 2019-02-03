from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post


def home_view(request):
    posts = Post.objects.all()[::-1]
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def edit_view(request, post_id):
    if (request.method == 'POST'):
        post = Post.objects.get(pk=post_id)
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.published_at = timezone.now()
        post.save()
        return redirect('/blog/detail/' + str(post.id))

    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'blog/edit.html', context)


def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/blog/')


def new_view(request):
    if (request.method == 'POST'):
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.published_at = timezone.now()
        post.save()
        return redirect('/blog/detail/' + str(post.id))

    return render(request, 'blog/new.html')
