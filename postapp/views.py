from django.shortcuts import render,redirect
from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

def GetPosts(request):
    posts=Post.objects.all()
    return render(request, 'postapp/list.html', context={"posts":posts})


def GetPost(request, pk):
    template_name = 'postapp/detail.html'
    post = Post.objects.get(pk=pk)
    comments = post.comments.filter(parent__isnull=True)  # faqat asosiy commentlar
    comment_form = CommentForm()

    tags= post.tags.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_id = request.POST.get("ParentId")
            parent_obj = None
            if parent_id:
                try:
                    parent_obj = Comment.objects.get(pk=parent_id)
                except Comment.DoesNotExist:
                    parent_obj = None

            cf = comment_form.save(commit=False)
            cf.post = post
            cf.parent = parent_obj  # reply bo‘lsa parent qo‘yiladi, bo‘lmasa None
            cf.save()
            return redirect('post_detail', pk=post.pk)

    context = {
        "post": post,
        'comment_form': comment_form,
        'comments': comments,
        'tags':tags
    }
    return render(request, template_name, context)


def GetPostsbyTag(request, tagName):
    filter=True
    template_name='postapp/list.html'
    posts_by_filter= Post.objects.filter(tags__name=tagName)

    context={'posts_by_filter':posts_by_filter}
    return render(request, template_name=template_name,context=context )