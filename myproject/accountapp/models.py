from django.db import models

class HelloWorld2(models.Model):
    text = models.CharField(max_length=255, null=False)