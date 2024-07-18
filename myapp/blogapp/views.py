from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from  django.http import Http404
# Create your views here.

#static demo data

# posts=[
#         {'id':1,'title':'Post 1','content':'Content Of Posts 1'},
#         {'id':2,'title':'Post 2','content':'Content Of Posts 2'},
#         {'id':3,'title':'Post 3','content':'Content Of Posts 3'},
#         {'id':4,'title':'Post 4','content':'Content Of Posts 4'},
#     ]
    
def index(request):
    blog_title='Latest Posts'
    #getting data from post model
    posts=Post.objects.all()
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})

def details(request,post_id):
    #static data
    # post=next((item for item in posts if item['id'] == int(post_id)),None)
    
    try:
        
        #getting data from model  by post id
        post=Post.objects.get(pk=post_id)
        
    except Post.DoesNotExist:
        raise Http404('Post Does Not Exits!')
    # logger=logging.getLogger('Testing')
    # logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blogapp:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new url")