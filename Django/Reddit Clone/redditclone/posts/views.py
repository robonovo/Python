from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, 'posts/create.html',
                          {'error': 'ERROR: You must include a Title and a URL to create a post'})
    else:
        return render(request, 'posts/create.html')


def home(request):
    posts = Post.objects.order_by('-votes_total')
    return render(request, 'posts/home.html', {'posts': posts})


def upvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total += 1
        post.save()
        author = request.POST.get('author', '')
        if request.POST.get('frompage') == 'home':
            return redirect('home')
        else:
            return redirect('posts:byuser', author=author)


def downvote(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.votes_total -= 1
        post.save()
        author = request.POST.get('author', '')
        if request.POST.get('frompage') == 'home':
            return redirect('home')
        else:
            return redirect('posts:byuser', author=author)


def byuser(request, author):
    posts = Post.objects.filter(author__username=author).order_by('-votes_total')
    return render(request, 'posts/byuser.html', {'posts': posts, 'author': author})
