from django.shortcuts import render
from articles.models import Blog

# Create your views here.

def home (request):
    """
    Welcome page for our fintech application
    """
    all_posts = Blog.objects.all()
    context = {
        'all_posts':all_posts,
    }
    return render(request, 'pages/index.html', context)
