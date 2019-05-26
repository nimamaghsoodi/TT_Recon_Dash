from django.urls import path, include
from RDApp import views

app_name = 'RDApp'

urlpatterns =[
    path('MonitorHome/',views.MonitorHome,name='MonitorHome'),
    path('UpdateHome/',views.UpdateHome,name='UpdateHome'),
    path('UpdateReg/',views.UpdateReg,name='UpdateReg'),
    path('UpdateLoggedIn/',views.user_login,name='UpdateLoggedIn'),
    path('RecUpdated/',views.RecUpdated,name='RecUpdated'),
    path('MonitorQuery/',views.monitor_user_login,name='MonitorQuery'),
    path('MonitorQueryResult/',views.monitor_query_result,name='MonitorQueryResult'),
    path('MonitorQueryResultUser/',views.monitor_query_result_user,name='MonitorQueryResultUser'),
    path('MonitorQueryResultTimePeriod/',views.monitor_query_result_timeperiod,name='MonitorQueryResultTimePeriod'),
    path('ReconAssign/',views.ReconAssign,name='ReconAssign'),
    path('ReconAssignUpdate/',views.RecAssignUpdate,name='ReconAssignUpdate'),
    path('RecAssignDone/',views.RecAssignDone,name='RecAssignDone'),
    path('MonitorQueryResultRecType/',views.monitor_query_result_rectype,name='MonitorQueryResultRecType'),
    # path('accounts/login/', include('django.contrib.auth.urls')),
    # path('',views.query_recon_date,name=''),
]
