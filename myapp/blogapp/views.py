from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h2>Hello World,You are at blog's index</h2>")

def details(request,post_id):
    return HttpResponse(f"<h2>You are viewing post .And ID is {post_id}</h2>")

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This is the new url")