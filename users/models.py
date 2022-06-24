import email
from multiprocessing import parent_process
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	'''
	Our UserProfile model extends the built-in Django User Model
	'''
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	address = models.CharField(verbose_name="Address",max_length=100, null=True, blank=True)
	town = models.CharField(verbose_name="Town/City",max_length=100, null=True, blank=True)
	county = models.CharField(verbose_name="County",max_length=100, null=True, blank=True)
	post_code = models.CharField(verbose_name="Post Code",max_length=8, null=True, blank=True)
	country = models.CharField(verbose_name="Country",max_length=100, null=True, blank=True)
	longitude = models.CharField(verbose_name="Longitude",max_length=50, null=True, blank=True)
	latitude = models.CharField(verbose_name="Latitude",max_length=50, null=True, blank=True)
	has_profile = models.BooleanField(default = False)

	def __str__(self):
		return f'{self.user}'


class Student(models.Model):
	'''
	Our Student model extends the Foreign key of Userprofile Model
	'''
	CHOICES_REL = (
			('Father', 'Father'),
			('Mother', 'Mother'),
			('Guardian', 'Guardian')
			) 
	CHOICES_CLASS = (
		('Nursery & Kindergarten','Nursery & Kindergarten'),
		('Standard 1','Standard 1'),
		('Standard 2','Standard 2'),
		('Standard 3','Standard 3'),
		('Standard 4','Standard 4'),
		('Standard 5','Standard 5'),
		('Standard 6','Standard 6'),
		('Standard 7','Standard 7')
	)
	student = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	stud_name = models.CharField(max_length=100, null=True, blank=True)
	parent_name = models.CharField(max_length=100, null=True, blank=True)
	relationship = models.CharField(max_length=50, null=True, choices=CHOICES_REL)
	classroom = models.CharField(max_length=50, null=True, choices=CHOICES_CLASS)
	parent_phone = models.CharField(max_length=15, null=True)
	email = models.EmailField(max_length=50, null=True, blank=True)
	is_active = models.BooleanField(default = True)

	def __str__(self):
		return f'{self.student}'


class Employee(models.Model):
	'''
	Our Employees model extends the Foreign key of Userprofile Model
	'''
	CHOICES_TYPE = (
			('Teacher', 'Teacher'),
			('Driver', 'Driver'),
			('Attendant', 'Attendant'),
			('Other', 'Other'),
		) 
	employee = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	name = models.CharField(max_length=70, null=True, blank=True)
	type = models.CharField(max_length=50, null=True, choices=CHOICES_TYPE)

	def __str__(self):
		return f'{self.employee}'

