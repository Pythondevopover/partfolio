from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Telefon raqami", blank=True, null=True)
    message = models.TextField(verbose_name="Xabar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    def __str__(self):
        return f"{self.name} - {self.email}"
