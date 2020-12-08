from django.db import models


class Data(models.Model):
    temp = models.CharField(max_length=4)
    moist = models.CharField(max_length=4)
