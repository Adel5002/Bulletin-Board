from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True,  null=True)
    slug = models.SlugField(null=True, unique=True, db_index=True)
    dateCreation = models.DateTimeField(auto_now_add=True)
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    upload = models.FileField(upload_to='uploads/', blank=True, default='/media/images/pngwing.com.png')

    def __str__(self):
        return f'{self.title}  {self.body}'

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    commentator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


