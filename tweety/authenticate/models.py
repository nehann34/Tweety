from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserToken(models.Model):
	screen_name=models.CharField(max_length=100)
	yellowant_token=models.CharField(max_length=100)
	yellowant_id=models.IntegerField(default=0)
	yellowant_integration_id=models.IntegerField(default=0)