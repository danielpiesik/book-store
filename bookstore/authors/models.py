import datetime

from django.db import models

from utils.nationalities import NATIONALITIES


class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthday = models.DateField()
    nationality = models.CharField(max_length=2, choices=NATIONALITIES)

    def calculate_age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25)

    def prepare_name(self):
        return f'{self.first_name} {self.last_name}'

    age = property(calculate_age)
    name = property(prepare_name)

    def __str__(self):
        return self.name
