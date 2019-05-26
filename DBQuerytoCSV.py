import pandas as pd
import datetime

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ReconDashboard.settings')

import django
django.setup()

from RDApp.models import NewReconUpdate,ReconAssignment
from pandas.io.json import json_normalize

# Records = NewReconUpdate.objects.filter(ReconType='Daily').order_by('-ReconDateTime').values()

def DBQuerytoCSV(queryRes):

    indx =0
    for each in queryRes:

        df = json_normalize(each)
        df = df.drop(columns="id")
        indx += 1
        fileName = str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")) + "_Export.csv"
        df.to_csv('/media/%s'%fileName,mode='a',index=False, header=indx==1)

        # print(each)
