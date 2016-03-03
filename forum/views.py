from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Thread

def thread_list(request):
    thread = Thread.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/thread_list.html', {'thread': thread})