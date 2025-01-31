from django.db import models

from common.models import User

# Create your models here.
class AccessLevel(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    MANAGER = 'MANAGER', 'Manager'
    DEVELOPER = 'DEVELOPER', 'Developer'
    EMPLOYEE = 'EMPLOYEE', 'Employee'
    REVIEWER = 'REVIEWER', 'Reviewer'
    SHAREHOLDER = 'SHAREHOLDER', 'Shareholder'
    MARKETING = 'MARKETING', 'Marketing'
    ACCOUNTANT = 'ACCOUNTANT', 'Accountant'

class Admin(User):
    designation = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)
    profile_updated_at = models.DateTimeField(auto_now=True)
    acceess_level = models.CharField(max_length=10, choices=AccessLevel.choices)

    def __str__(self):
        return self.username