from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class teacher(models.Model):
	name = models.CharField(max_length=50)
	no = models.CharField(max_length=50)
	

	def __str__(self):
		return self.name
class student(models.Model):
	created = models.OneToOneField(User, on_delete=models.CASCADE)
	#code = models.CharField(max_length=10,unique=True)
	review= models.CharField(max_length=50)
	EVENT_CHOICES = (
        ('E', 'Excellent'),
        ('G', 'Good'),
        ('A', 'Average'),
        ('P', 'Poor'),
  )
	question = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES,
        default='G',
        blank=False,
  )
	EVENT_CHOICES1 = (
        ('E1', 'Excellent'),
        ('G1', 'Good'),
        ('A1', 'Average'),
        ('P1', 'Poor'),
  )
	question1 = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES1,
        default='G1',
        blank=False,
  )
	EVENT_CHOICES2 = (
        ('E2', 'Excellent'),
        ('G2', 'Good'),
        ('A2', 'Average'),
        ('P2', 'Poor'),
  )
	question2 = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES2,
        default='G2',
        blank=False,
  )
	EVENT_CHOICES3 = (
        ('E3', 'Excellent'),
        ('G3', 'Good'),
        ('A3', 'Average'),
        ('P3', 'Poor'),
  )
	question3 = models.CharField(
        max_length=10,
        choices=EVENT_CHOICES3,
        default='G3',
        blank=False,
  )
	

	def __str__(self):
		return "Profile of user {}".format(self.created.username)