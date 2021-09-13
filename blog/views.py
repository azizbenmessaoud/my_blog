from blog.models import Post
from django.shortcuts import render
from django.views import generic

'''
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
'''

def postList(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/index.html', {'post_list': posts})

def postDetail(request, slug):
    posts = Post.objects.filter(slug=slug)
    post = posts[0]
    return render(request, 'blog/post_detail.html', {'post': post})