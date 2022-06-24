from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from ckeditor.fields import RichTextField

class Suggestion(models.Model):
    Subject=models.CharField(max_length=1000)
    Description=FroalaField(default="",options={"height":200,"placeholderText":"Place write your Suggestion and all here....",'autofocus': True,'attribution': False})
    # image=models.ImageField(upload_to="app/images",default="")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    post_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Subject

