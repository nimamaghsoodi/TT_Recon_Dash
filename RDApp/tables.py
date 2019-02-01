import django_tables2 as tables
from RDApp.models import ReconUpdate

class ResultTable(tables.Table):
    class Meta:
        model = ReconUpdate
        template_name = 'RDApp/MonitorQueryResult.html'
