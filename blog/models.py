from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
        

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ["date_added"]
