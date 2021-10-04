from django.db import models
from django.contrib.auth.models import User


class Demo(models.Model):
    FRAMEWORK_CHOICES = [
        ('Tensorflow', 'Tensorflow'),
        ('Pytorch', 'Pytorch'),
        ('Caffe', 'Caffe'),
    ]
    
    TASK_CHOICES = [
        ('Segmentation', 'Segmentation'),
        ('Object Detection', 'Object Detection'),
        ('Keypoint Detection', 'Keypoint Detection'),
        ('Classification', 'Classification'),
        ('GAN', 'GAN'),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_demo')
    photo = models.ImageField(blank=True, upload_to="demo/%Y/%m/%d")
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    framework = models.CharField(max_length=10, choices=FRAMEWORK_CHOICES)
    task = models.CharField(max_length=20, choices=TASK_CHOICES)
    url = models.URLField("Site URL")
    voter = models.ManyToManyField(User, related_name='voter_demo')