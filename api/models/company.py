from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    tax_code = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk and Company.objects.exists():
            raise ValueError("There can be only one Company instance.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.tax_code})"