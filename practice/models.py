from django.db import models
# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=10)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

