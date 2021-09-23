from django.db import models

# Create your models here.
class contractForm(models.Model):
        user = models.CharField(max_length=100)
        email = models.EmailField()
        body = models.TextField()
        def __str__(self):
                return self.email
