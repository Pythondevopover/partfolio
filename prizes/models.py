from django.db import models

# Create your models here.
class Prize(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    awarded_on = models.DateField()
    photo = models.ImageField(upload_to='static/image/')

    def __str__(self):
        return self.name