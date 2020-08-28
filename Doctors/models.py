from django.db import models
from django.utils import timezone
from django.conf import settings


class Doctor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1,
                             on_delete=models.DO_NOTHING,
                             )

    d_name = models.CharField(max_length=50)
    d_address = models.TextField()
    speciality = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=15, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True,
                              blank=True
                              )

    def __str__(self):
        return "{}".format(self.d_name)
