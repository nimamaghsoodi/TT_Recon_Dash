from django.db import models
import datetime

# Create your models here.

class ReconUpdate(models.Model):
    ReconTitle = models.CharField(max_length=100)
    RespPers = models.CharField(max_length=30)
    ReconTotalCount = models.IntegerField()
    ReconExecutedCount = models.IntegerField()
    ReconDate = models.DateField()
    # UpdateDate = models.CharField(max_length=30)
    # UserId = models.CharField(max_length=10)

class AccessRecord(models.Model):
    LoggedInUser = models.CharField(max_length=20)
    LoggedInDate = models.DateField()
