from django.db import models

# Create your models here.

class Job(models.Model):
    """docstring for Job.models.Model
    def __init__(self, arg):
        super(Job,models.Model).__init__()
        self.arg = arg
    """

    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
