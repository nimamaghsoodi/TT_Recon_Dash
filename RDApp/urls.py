from django.urls import path
from RDApp import views

app_name = 'RDApp'

urlpatterns =[
    path('MonitorHome/',views.MonitorHome,name='MonitorHome'),
    path('UpdateHome/',views.UpdateHome,name='UpdateHome'),
    path('UpdateReg/',views.UpdateReg,name='UpdateReg'),
    path('UpdateLoggedIn/',views.user_login,name='UpdateLoggedIn'),
    path('RecUpdated/',views.RecUpdated,name='RecUpdated'),
    path('MonitorQuery/',views.monitor_user_login,name='MonitorQuery'),
    path('MonitorQueryResult/',views.monitor_query_result,name='MonitorQueryResult')
    # path('',views.query_recon_date,name=''),
]
