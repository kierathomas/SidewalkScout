from django.contrib.auth.models import AbstractUser
from django.db import models

# Sidewalk Models:
class Sidewalk(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"ID: {self.id}, Score: {self.score}"

class Metrics(models.Model):
    sidewalk = models.ForeignKey(Sidewalk, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    speed_limit = models.IntegerField()
    pedestrian_deaths = models.IntegerField()

    def __str__(self):
        return f"ID: {self.sidewalk_id}, Latitude: {self.latitude}, Longitude: {self.longitude}, Speed Limit: {self.speed_limit}, Pedestrian Deaths: {self.pedestrian_deaths}"

# Authentication Models:
    
# The following fields are inherited: "email", "password", "username"; may switch to AbstractBaseUser if auth requirements become more complicated
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
