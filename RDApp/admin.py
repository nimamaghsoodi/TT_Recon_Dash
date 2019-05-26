from django.contrib import admin
from RDApp.models import ReconUpdate,AccessRecord,ReconAssignment,NewReconUpdate

# Register your models here.

admin.site.register(ReconUpdate)
admin.site.register(AccessRecord)
admin.site.register(ReconAssignment)
admin.site.register(NewReconUpdate)
