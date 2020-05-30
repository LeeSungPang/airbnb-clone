from django.db import models


class TimeStampeModel(models.Model):

    """ Time Stampe Model"""

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True
