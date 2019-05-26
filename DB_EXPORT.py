from django.db import connection
import pandas as pd

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ReconDashboard.settings')

import django
django.setup()

from RDApp.models import ReconUpdate,NewReconUpdate,ReconAssignment



df = pd.DataFrame(list(ReconAssignment.objects.all().values()))
df.to_csv('RecAssign_Exported.csv', sep=',')
