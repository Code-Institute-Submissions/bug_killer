from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('d', 'done'),
    ('n', 'nothing'),
    ('w', 'working'),
)


DONE = 'D'
LOOKING = 'L'
WORKING = 'W'

STATUS_OPTIONS=(
    ('D', 'Done'),
    ('L', 'Looking'),
    ('W', 'Working'),
    )


class Post(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)

    status_options = models.CharField(max_length=1, choices=STATUS_OPTIONS,  null=True, blank=True)
    title = models.CharField(max_length=200,)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    
    def __str__(self):
        return self.title
        
class Status(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='status')

    def __str__(self):
        return self.title