from django.db import models


class Test(models.Model):
    email = models.CharField(max_length=25)


class Object(models.Model):
    tests = models.ManyToManyField(Test)
