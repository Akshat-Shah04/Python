from django.shortcuts import render,redirect
from .models import *
# Create your views here.
# method 1 using create()
def create(request):
    if request.method == "POST":
        post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],

        )
        return redirect('index')
    return render(request,"create.html")
'''
# method 2 : using save()
def savePost(request):
    if request.method == "POST":
        post = Post(title="Post 1",content="ckjw ishiusi udsaiufh sis fs")
        post.save()
        return redirect('index')
    return render(request,"create.html")
'''

def index(request):
    post = Post.objects.all()
    return render(request,"index.html",{'posts':post})