from django.db import connection

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ReconDashboard.settings')

import django
django.setup()

from RDApp.models import NewReconUpdate,ReconAssignment
# NewReconUpdate.objects.all().delete()
# ReconAssignment.objects.all().delete()

# cursor = connection.cursor()
# cursor.execute("TRUNCATE TABLE 'ReconUpdate'")
