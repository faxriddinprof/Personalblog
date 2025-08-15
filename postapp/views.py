from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import CommentForm
# Create your views here.

def GetPosts(request):
    posts=Post.objects.all()
    return render(request, 'postapp/list.html', context={"posts":posts})



def GetPost(request, pk):
    template_name='postapp/detail.html'
    post=Post.objects.get(pk=pk)
    comments=post.comments.all()
    comment_form=CommentForm()

    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            cf=comment_form.save(commit=False)
            cf.post.id= post.id
            cf.save()


    context={"post":post, 'comment_form':comment_form, 'comments':comments}
    return render(request, template_name=template_name, context=context)