from django.db import models

# Create your models here.
class UserRank(models.Model):
    site_name = models.CharField(max_length=255)  # Sayt nomi
    rank = models.PositiveIntegerField()  
    photo = models.ImageField(upload_to='static/image/')
    score = models.PositiveBigIntegerField()
    rank_name = models.CharField(max_length=255)
    profil = models.CharField(max_length=255)
    profil_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.site_name} - Rank: {self.rank} - Rating: {self.photo}"