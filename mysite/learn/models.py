from django.db import models


# Create your models here.

### for picture ! 
class Post(models.Model):
    photo = models.URLField(blank=True)
    def __str__(self):
        return self.title
