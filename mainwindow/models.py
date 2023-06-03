from django.db import models



class Resume(models.Model):
    user_id = models.IntegerField()
    path = models.TextField()
