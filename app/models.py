from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ValidationError
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default = False)
    updated_at = models.DateTimeField(null=True, blank=True)
    body = RichTextUploadingField(default="content")
    author_name = models.CharField(max_length=255, null=True, blank=True)
    author_profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    readtime = models.CharField(max_length=255,null=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

        
    class Meta:
        ordering = ['-updated_at']

    def save(self, *args, **kwargs):
        if not self.updated_at:
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)


    def formatted_updated_at(self):
        return self.updated_at.strftime('%b. %d, %Y').replace(' 0', ' ')    


    def _str_(self):
        if(self.is_draft):
            return  self.title +' | ' + str(self.author) +' | Draft | ' + self.updated_at.strftime("%d/%m/%Y")
        return  self.title +' | ' + str(self.author) + ' | ' + self.updated_at.strftime("%d/%m/%Y")

class BlogMedia(models.Model):
    blog = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="media")
    file = models.ImageField(upload_to='image')

    def _str_(self):
        return self.blog.title
        
class BlogComment(models.Model):
    blog = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()  
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def formatted_updated_at(self):
        return self.updated_at.strftime('%b. %d, %Y')     

    # def _str_(self):
    #     return self.name | self.comment