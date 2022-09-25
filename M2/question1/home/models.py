from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class toDo(models.Model):
    title=models.CharField(max_length=100, default="ToDo:")
    description=models.CharField(max_length=500, null=True, blank=True)
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "To-Do"
