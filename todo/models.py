from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class Todo(models.Model):
    todo = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='todos')
    is_completed = models.BooleanField(default=False, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo