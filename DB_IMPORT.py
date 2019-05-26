import pandas as pd
import datetime

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ReconDashboard.settings')

import django
django.setup()

from RDApp.models import NewReconUpdate,ReconAssignment

# with open('UsersReconList.csv','r') as f:
#     RESULT = f.readlines()
#
# for each in RESULT:
#     print(each)
#
#     try:
#
#         eachlisted = each.split(",")
#
#         NewRecord = ReconAssignment(DefinedUser=eachlisted[0],UserFullName=eachlisted[-1].split("\n")[0],UserReconTitle=eachlisted[1],UserReconType=eachlisted[2],OccuranceNum=int(eachlisted[-2]))
#         NewRecord.save()
#
#     except Exception as err:
#         print("DB not updated for following record: %s"%each)
#         continue



# RESULT = pd.read_csv('ReconUpdate_Exported.csv')

# print(RESULT)

# for each in RESULT.iterrows():
#     print(each[1])

# with open('ReconUpdate_Exported.csv','r') as f:
#     RESULT = f.readlines()
#
# # RESULT = ["4/23/19,100,posting 2 requests at the same time (simc/ revoke),162,marzieh zolghadrian,marzieh.zo"]
#
# for each in RESULT:
#
#     try:
#
#         converted_each_date = datetime.datetime.strptime(each.split(",")[0],'%m/%d/%y')
#         eachlisted = each.split(",")
#         print(eachlisted)
#
#         NewRecord = NewReconUpdate(ReconUser=eachlisted[-1].split("\n")[0],ReconTitle=eachlisted[2],ReconTotalCount=int(eachlisted[3]),ReconExecutedCount=int(eachlisted[1]),ReconType=eachlisted[-2],ReconDateTime=converted_each_date)
#         NewRecord.save()
#
#     except Exception as err:
#         print("Error occured for following record: %s"%each)
#         print(err)
#         continue
