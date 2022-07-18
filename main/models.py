from django.db import models


class Test(models.Model):
    email = models.CharField(max_length=25)
