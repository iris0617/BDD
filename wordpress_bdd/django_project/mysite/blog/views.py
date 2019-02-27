from blog.models import Blog
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html', {'blogs':blog_list})

def blog_data(request):
    blog_list = Blog.objects.all()
    print(blog_list)
    dicts = {}
    for blog in blog_list:
        dicts[blog.title] = blog.body
    j = json.dump(dicts)
    return HttpResponse(j)