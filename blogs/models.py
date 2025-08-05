from django.db import models
from django.utils import timezone

class BlogCategory(models.Model):  
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)  # ✅ FIXED
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
