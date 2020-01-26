from django.db import models


class RustSource(models.Model):
    category = models.CharField(max_length=255)


class PythonSource(models.Model):
    category = models.CharField(max_length=255)
