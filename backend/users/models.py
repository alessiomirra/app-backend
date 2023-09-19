from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.

class CustomUser(AbstractUser):
    weight = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    food_plan = models.JSONField(blank=True, null=True)
    training_plan = models.JSONField(blank=True, null=True)
    weight_history = models.JSONField(blank=True, null=True)


class Objective(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="objectives")
    objective = models.TextField()
    reached = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Objective by " + self.user.username 

