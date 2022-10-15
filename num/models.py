
from django.db import models
import random


def random_string():
    return str(random.randint(0, 100))


class Numbers(models.Model):
    num_1 = models.CharField(max_length=3, default=random_string)
    num_2 = models.CharField(max_length=3, default=random_string)
    num_3 = models.CharField(max_length=3, default=random_string)
    num_4 = models.CharField(max_length=3, default=random_string)
    num_5 = models.CharField(max_length=3, default=random_string)
    num_6 = models.CharField(max_length=3, default=random_string)
    num_7 = models.CharField(max_length=3, default=random_string)
    num_8 = models.CharField(max_length=3, default=random_string)
    num_9 = models.CharField(max_length=3, default=random_string)
    num_10 = models.CharField(max_length=3, default=random_string)
