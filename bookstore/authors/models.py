import datetime

from django.db import models

from utils.nationalities import NATIONALITIES


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthday = models.DateField()
    nationality = models.CharField(max_length=2, choices=NATIONALITIES)

    @property
    def age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.name
