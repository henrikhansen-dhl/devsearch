from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.URLField(max_length=200, null=True, blank=True)
    source_link = models.URLField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # Owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=4, choices=VOTE_TYPE, default='up')    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)    
    
    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name    