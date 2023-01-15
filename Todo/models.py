from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=255,null=False,blank=False)
    done = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True,null=False,blank=False)
    user = models.ForeignKey(User,related_name='User',on_delete=models.CASCADE,null=False,blank=False)

    def __str__(self) -> str:
        return  f"{self.title} : {self.date} - Done :{self.done}"