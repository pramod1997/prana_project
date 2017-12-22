# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):
	document=models.FileField(upload_to='prana/')
	uploaded_at=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.FileField.name


class FileName(models.Model):
	upload_file_name=models.CharField(max_length=255)
	def __str__(self):
		return self.FileName.name



class Advance(models.Model):
	hw_param1 = models.FloatField(default=0.0)
	hw_param2 = models.FloatField(default=0.0)
	hw_param3 = models.FloatField(default=0.0)

	c_param1  = models.FloatField(default=0.0)
	c_param2  = models.FloatField(default=0.0)


	fb_prophet_param1 = models.FloatField(default = 0.0)

	arima_param1 = models.FloatField(default=0.0)
	def __str__(self):
		return 













