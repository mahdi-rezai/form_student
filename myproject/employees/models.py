from django.db import models

class employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    tittlejob = models.CharField(max_length=100)
    password = models.CharField(max_length=128)  # فیلد رمز عبور اضافه شد

    def __str__(self):
        return f"{self.first_name} {self.last_name}"