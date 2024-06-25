from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Calculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expression = models.CharField(max_length=255)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.expression} = {self.result}'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calculations = models.ManyToManyField(Calculation, related_name='user_profiles')

    def __str__(self):
        return self.user.username
