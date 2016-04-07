
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Thread
from .forms import PostForm, ThreadForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .serializers import ThreadSerializer, PostSerializer
from rest_framework import generics


class APIThreadList(generics.ListCreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer



def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'forum/thread_list.html', {'threads': threads})

def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})

def thread_new(request):
    add_thread = ThreadForm()
    return render(request, 'forum/thread_edit.html', {'form': form})

def thread_new(request):
    if request.method == "POST":
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.save()
            return redirect('thread_detail', pk=thread.pk)
    else:
        form = ThreadForm()
    return render(request, 'forum/thread_edit.html', {'form': form})


def post_list(request):
    posts = Post.objects.filter(last_edited_date__lte=timezone.now()).order_by('last_edited_date')
    return render(request, 'forum/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/post_details.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})

@login_required
def post_new(request, pk):
    # decorator code will run here
    if request.method == "POST":
        form = PostForm(request.POST)
        thread = get_object_or_404(Thread, pk=pk)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.last_edited_date = timezone.now()
            post.thread = thread
            post.save()
            return redirect('post_detail', pk=post.pk)

            
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})




