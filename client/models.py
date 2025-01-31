from django.db import models

from common.models import Job, User

# Create your models here.
class Client(User):
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()

    def __str__(self):
        return self.company_name

class Profile(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="client/")
    bio = models.TextField()
    joined_at = models.DateTimeField(auto_now_add=True)
    profile_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.company_name

class JobPost(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="client/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title