from django.db import models

# Create your models here.


class Post(models.Model):
    title= models.CharField(max_length=200)
    body = models.TextField()
    image= models.FileField(upload_to='images/')
    tags= models.ManyToManyField('Tag',related_name='tags', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'postapp'
        ordering=['-created_at']


    def __str__(self):
        return self.title
    

class Tag(models.Model):
    name= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Comment(models.Model):

    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    wibesite=models.CharField(max_length=200, blank=True, null=True)
    createt_at=models.DateTimeField(auto_now_add=True)
    message= models.TextField()
    parent= models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', blank=True, null=True)
    image= models.FileField(upload_to='comment_image', default='comment_image/user.png')

    # parent= models.ForeignKey('Comment', on_delete=models.CASCADE, related_name=)


    def __str__(self):
        return self.name
    

    @property
    def getReplies(self):
        return Comment.objects.filter(parent=self).order_by('-createt_at')
    
    @property
    def isParent(self):
        if self.parent is None:
            return True
        return False