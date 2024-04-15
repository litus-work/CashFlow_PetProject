from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.manager import BaseManager


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)

    # Изменяем обратные связи для групп и разрешений
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',  # Новое имя обратной связи для групп
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',  # Новое имя обратной связи для разрешений
        related_query_name='custom_user'
    )


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    objects = None
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.description} - {self.category}"
