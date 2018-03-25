from django.db import models
 
# Create your models here.
class apitable(models.Model):
	screen_name=models.CharField(max_length=100)
	twitter_oauth_token=models.CharField(max_length=100)
	twitter_oauth_verifier=models.CharField(max_length=100)
	twitter_access_token_key=models.CharField(max_length=100)
	twitter_access_token_secret=models.CharField(max_length=100)