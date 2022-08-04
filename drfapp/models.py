from django.db import models


class Army(models.Model):
    name = models.CharField(max_length=40)
    batallion = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
