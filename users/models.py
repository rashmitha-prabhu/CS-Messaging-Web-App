from django.db import models

# Create your models here.

class UserQuery(models.Model):
    userID = models.PositiveSmallIntegerField("User ID")
    timestamp = models.DateTimeField("Timestamp (UTC)", auto_now_add=True)
    messageBody = models.TextField("Message Body")
