import pandas as pd
import datetime

print(str(datetime.datetime.now().date()))

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ReconDashboard.settings')

import django
django.setup()

from RDApp.models import NewReconUpdate,ReconAssignment

allRecords = NewReconUpdate.objects.all()
for each in allRecords:
    each.ReconComments = " "
    each.save()

# dailyRecords = NewReconUpdate.objects.filter(ReconType='Daily')
# dailyList = list()
# dailyListObj = list()
# for each in dailyRecords:
#     dailyList.append(each.ReconTitle)
#     dailyListObj.append(each)
#
# todayDoneList = list()
# todayRecords = NewReconUpdate.objects.filter(ReconDateTime__gte=str(datetime.datetime.now().date()))
# for each in todayRecords:
#     todayDoneList.append(each.ReconTitle)
#
# for each in dailyList:
#     # print(each)
#     if each not in todayDoneList:
#         print(each)
#         indx = dailyList.index(each)
#         mem = dailyListObj[indx]
#         newObj = NewReconUpdate(ReconUser=mem.ReconUser,ReconTitle=mem.ReconTitle,ReconTotalCount=0,ReconExecutedCount=0,ReconType="Daily",ReconDateTime=(datetime.datetime.now()+ datetime.timedelta(hours=4,minutes=30)))
#         newObj.save()
