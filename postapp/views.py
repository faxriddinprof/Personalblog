from django.shortcuts import render,redirect
from .models import Post, Comment
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
    if request.method =='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            parent_obj= None
            try:
                parent_id= request.POST.get("ParentId")
            except:
                parent_id=None
                
            if parent_id:
                parent_obj = Comment.objects.get(pk=parent_id)
            if parent_obj:
                cf =comment_form.save(commit=False)
                cf.parent=parent_obj
                cf.post=post
                cf.save()
                return redirect('post_detail', pk=post.pk)



    context={"post":post, 'comment_form':comment_form, 'comments':comments}
    return render(request, template_name=template_name, context=context)