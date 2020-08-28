from django.db import models
from django.utils import timezone 
from django.conf import settings

class Patient(models.Model):

	p_name = models.CharField(max_length=50)
	p_age = models.IntegerField(default=0)
	p_sex = models.CharField(max_length=10,default=None)
	contact_no = models.CharField(max_length=15,default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 default=1,
							 on_delete=models.DO_NOTHING,
							)
	p_address = models.TextField()
	disease = models.CharField(max_length=100)
	ward_no = models.CharField(max_length=50)
	timestamp = models.DateTimeField(auto_now_add=True)

	


	def __str__(self):
		return "{}".format(self.p_name)

