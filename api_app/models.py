from django.db import models

# Create your models here.


class Todo(models.Model):
    task_name = models.CharField(max_length=50)
    task_description = models.CharField(max_length=200)
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(max_length=50)
    task_assigned_to = models.CharField(max_length=50)
    task_status = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name + ' | ' + self.task_assigned_to
