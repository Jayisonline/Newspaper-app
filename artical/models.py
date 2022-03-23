from datetime import date
from django.db import models
from matplotlib.pyplot import title


from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField

# Create your models here.



class Artical(models.Model):
    title = FroalaField(max_length=225)
    # body = models.TextField()
    body = FroalaField(blank = True)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete= models.CASCADE,
    )


    def __str__(self) -> str:
        return self.title


    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])



class Comment(models.Model):
    article = models.ForeignKey(Artical, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        related_name='comments', 
    )


    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('article_list')

