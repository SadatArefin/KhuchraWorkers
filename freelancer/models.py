from django.db import models

from client.models import Client, Job, JobPost
from common.models import User

# Create your models here.
class Freelancer(User):
    skills = models.TextField()
    bio = models.TextField()
    joined_at = models.DateTimeField(auto_now_add=True)
    profile_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Projects (models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="freelancer/")

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    user = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="freelancer/")
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.title

class Bid(models.Model):
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    proposal = models.TextField()
    bid_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount

class Deliverable(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to="freelancer/deliverables/")
    delivered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deliverable