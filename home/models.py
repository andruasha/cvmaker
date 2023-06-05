from django.db import models


class Summary(models.Model):
    name = models.CharField(max_length=128, blank=False)
    path = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name