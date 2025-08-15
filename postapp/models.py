from django.db import models

# Create your models here.


class Post(models.Model):
    title= models.CharField(max_length=200)
    body = models.TextField()
    image= models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'postapp'
        ordering=['-created_at']


    def __str__(self):
        return self.title
    

class Comment(models.Model):

    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    wibesite=models.CharField(max_length=200, blank=True, null=True)
    createt_at=models.DateTimeField(auto_now_add=True)
    reply= models.ForeignKey('self', on_delete=models.CASCADE, related_name='leplies', null=True)
    message= models.TextField()


    def __str__(self):
        return self.name