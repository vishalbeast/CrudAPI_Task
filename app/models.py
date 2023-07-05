from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Additional fields for user information
    # For example:
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    # Other relevant fields

    def __str__(self):
        return self.username


class Post(models.Model):
    # post ID is automatically created as the primary key by Django
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    # Other relevant fields

    def __str__(self):
        return self.title


class Like(models.Model):
    # like ID is automatically created as the primary key by Django
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other relevant fields

    def __str__(self):
        return f"Like {self.id} by {self.user.username} on Post {self.post.title}"




# Create your models here.
#class User(models.Model):
#    user_name = models.CharField(max_length=100)
#    user_email = models.EmailField()
#    user_password = models.IntegerField()
#    
#class Post(models.Model):
#    post_title = models.CharField(max_length=50)
#    post_description = models.CharField(max_length=100)
#    post_content = models.CharField(max_length=100)
#    post_creation_date = models.DateTimeField()
#    
#
##class Like(models.Model):
##    like_ID = models.IntegerField()
##    user_ID = models.ForeignKey(on_delete=models.CASCADE)
##    post_ID = models.ForeignKey(on_delete=models.CASCADE)
##    
