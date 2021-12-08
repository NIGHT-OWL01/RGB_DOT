from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices

# Create your models here.
from multiselectfield import MultiSelectField

class tractor(models.Model):
    name= models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    MY_CHOICES = (
        ('a', 'Harrow'),
        ('b', 'Cultivator'),
        ('c', 'Rotavator'),
        ('d', 'Paddy Thrasher'),
        ('e', 'Dumping Trailer'),
        ('f', '4 wheel Trailer'),
    )
    implement = MultiSelectField(choices=MY_CHOICES)

    def __str__(self):
        return self.name


class implements(models.Model):
    name = models.CharField(default='no', max_length=20)
    belong_to = models.ForeignKey(tractor, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

