from django.db import models
import datetime

# Create your models here.

class ReconUpdate(models.Model):
    ReconTitle = models.CharField(max_length=100)
    RespPers = models.CharField(max_length=30)
    ReconTotalCount = models.IntegerField()
    ReconExecutedCount = models.IntegerField()
    ReconDate = models.DateField()
    ReconTime = models.TimeField()
    ReconType = models.CharField(max_length=30)
    # UpdateDate = models.CharField(max_length=30)
    # UserId = models.CharField(max_length=10)

class AccessRecord(models.Model):
    LoggedInUser = models.CharField(max_length=20)
    LoggedInDate = models.DateField()

class ReconAssignment(models.Model):
    DefinedUser = models.CharField(max_length=30)
    UserFullName = models.CharField(max_length=50)
    UserReconTitle = models.CharField(max_length=100)
    UserReconType = models.CharField(max_length=15)
    OccuranceNum = models.IntegerField()


class NewReconUpdate(models.Model):
    ReconUser = models.CharField(max_length=30,default='')
    ReconTitle = models.CharField(max_length=100,default='')
    ReconTotalCount = models.IntegerField(default='')
    ReconExecutedCount = models.IntegerField(default='')
    ReconType = models.CharField(max_length=20,default='')
    ReconDateTime = models.DateTimeField(default='')
    ReconComments = models.CharField(max_length=200,null=True,blank=True)
