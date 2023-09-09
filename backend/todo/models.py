from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    #set to current time
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    #user who posted the todo
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.title