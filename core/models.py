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


from django.db import models


class Budget(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    house_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    education = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    transportation = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    food = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    entertainment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    utilities = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    travel = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    communication = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sport = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    household = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    healthcare = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class BudgetCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='budget_categories')

    def __str__(self):
        return self.name
