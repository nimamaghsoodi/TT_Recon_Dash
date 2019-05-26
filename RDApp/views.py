from django.shortcuts import render
from RDApp.forms import UserForm,ReconUpdateForm,QueryDateForm,ReconAssignForm,NewReconUpdateForm,QueryUserForm,QueryTimePeriodForm,QueryRecTypeForm
from django import forms
import datetime
from RDApp.models import ReconUpdate,NewReconUpdate,ReconAssignment
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django_tables2 import RequestConfig
from RDApp.tables import ResultTable
from RDApp.decorators import recassgin_login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.utils import timezone
from DBQuerytoCSV import *

# Create your views here.

def index(request):
    return render(request,'RDApp/index.html',{})

def MonitorHome(request):
    return render(request,'RDApp/MonitorBase.html',{})

def UpdateHome(request):
    return render(request,'RDApp/UpdateBase.html',{})

def UpdateLoggedIn(request):
    return render(request,'RDApp/UpdateLoggedIn.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def UpdateReg(request):
    # return render(request,'RDApp/Register.html',{})
        registered = False
        if request.method == "POST":
            user_form = UserForm(data=request.POST)

            if user_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                registered = True
            else:
                print(user_form.errors)
        else:
            user_form = UserForm()

        return render(request,'RDApp/Register.html',{
                                            'user_form':user_form,
                                            'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active and user.groups.filter(name='ReconUpdate').exists():
                login(request,user)
                return HttpResponseRedirect(reverse('RDApp:RecUpdated'))    #reverse('admin:index'))
            else:
                NotPermitted = True
                return render(request,'RDApp/RecUpdateLogInPerm.html',{'NotPermitted':NotPermitted})
        else:
            print("SomeOne tried to login and failed!")
            print("username: {} and password {}".format(username,password))
            NotPermitted = False
            return render(request,'RDApp/RecUpdateLogInPerm.html',{'NotPermitted':NotPermitted})
    else:
        return render(request,'RDApp/UpdateLoggedIn.html',{})


@login_required
def RecUpdated(request):

    Updated = False

    if request.method == "POST":

        rec_update_form = NewReconUpdateForm(data=request.POST)
        # print(request.POST['ReconTitle'])

        if rec_update_form.is_valid():

            rec = rec_update_form.save(commit=False)
            rec.ReconUser = str(request.user.username)
            rec.ReconDateTime = datetime.datetime.now() + datetime.timedelta(hours=4,minutes=30)
            rec_assign_val = ReconAssignment.objects.filter(UserReconTitle=request.POST['ReconTitle']).values()
            rec.ReconType = rec_assign_val[0]['UserReconType']
            # print(rec_assign_val[0]['UserReconType'])
            rec.save()

            Updated = True

        else:
            print(rec_update_form.errors)

    else:
        rec_update_form = NewReconUpdateForm()

    return render(request,'RDApp/RecUpdated.html',{'rec_update_form':rec_update_form,
                                'Updated':Updated})


def monitor_user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active and user.groups.filter(name='Monitoring').exists():
                login(request,user)
                return HttpResponseRedirect(reverse('RDApp:MonitorQuery'))    #reverse('admin:index'))
            else:
                NotPermitted = True
                return render(request,'RDApp/MonitorLogInPerm.html',{'NotPermitted':NotPermitted})
        else:
            print("SomeOne tried to login into monitoring portal and failed!")
            print("username: {} and password {}".format(username,password))
            NotPermitted = False
            return render(request,'RDApp/MonitorLogInPerm.html',{'NotPermitted':NotPermitted})
    else:
        return render(request,'RDApp/MonitorQuery.html',{'query_date_form':QueryDateForm(),'query_user_form':QueryUserForm(),'query_timeperiod_form':QueryTimePeriodForm(),'query_rec_type_form':QueryRecTypeForm()})


@login_required
def monitor_query_result(request):

    if request.method == 'POST':
        if request.POST:
            rec_date_val = str(datetime.date(int(request.POST.get('query_date_year')),int(request.POST.get('query_date_month')),int(request.POST.get('query_date_day'))))
            request.session['rec_date_val'] = rec_date_val
            result_list_all = NewReconUpdate.objects.filter(ReconDateTime__gte=rec_date_val).order_by('-ReconDateTime')
        else:
            result_list_all = NewReconUpdate.objects.filter(ReconDateTime__gte=request.session['rec_date_val'])

    else:
        result_list_all = NewReconUpdate.objects.filter(ReconDateTime__gte=request.session['rec_date_val'])

    page = request.GET.get('page', 1)

    paginator = Paginator(result_list_all, 25)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    return render(request, 'RDApp/MonitorQueryResult.html', { 'result_list': result_list })
    # return render(request, 'RDApp/MonitorQueryResult.html', {'result_list': result_list_all})

@login_required
def monitor_query_result_user(request):

    if request.method == 'POST':
        if request.POST:
            rec_user_val = str(request.POST.get('query_user'))
            request.session['rec_user_val'] = rec_user_val
            result_list_all = NewReconUpdate.objects.filter(ReconUser=str(rec_user_val)).order_by('-ReconDateTime')
        else:
            result_list_all = NewReconUpdate.objects.filter(ReconUser=request.session['rec_user_val'])

    else:
        result_list_all = NewReconUpdate.objects.filter(ReconUser=request.session['rec_user_val'])

    page = request.GET.get('page', 1)

    paginator = Paginator(result_list_all, 25)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    return render(request, 'RDApp/MonitorQueryResultTimePeriod.html', { 'result_list': result_list })


@login_required
def monitor_query_result_timeperiod(request):

    if request.method == 'POST':
        # print(request.POST)
        if request.POST:
            rec_begin_date_val = str(datetime.date(int(request.POST.get('query_begin_date_year')),int(request.POST.get('query_begin_date_month')),int(request.POST.get('query_begin_date_day'))))
            rec_end_date_val = str(datetime.date(int(request.POST.get('query_end_date_year')),int(request.POST.get('query_end_date_month')),int(request.POST.get('query_end_date_day'))))
            request.session['rec_begin_date_val'] = rec_begin_date_val
            request.session['rec_end_date_val'] = rec_end_date_val

            result_list_all = NewReconUpdate.objects.filter(ReconDateTime__gte=rec_begin_date_val)
            result_list_all = result_list_all.filter(ReconDateTime__lte=rec_end_date_val)

        else:
            result_list_all = NewReconUpdate.objects.filter(ReconDateTime__gte=request.session['rec_begin_date_val'])
            result_list_all = result_list_all.filter(ReconDateTime__lte=request.session['rec_end_date_val'])

    else:
        result_list_all = NewReconUpdate.objects.filter(ReconDateTime__gte=request.session['rec_begin_date_val'])
        result_list_all = result_list_all.filter(ReconDateTime__lte=request.session['rec_end_date_val'])

    page = request.GET.get('page', 1)

    paginator = Paginator(result_list_all, 25)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    return render(request, 'RDApp/MonitorQueryResult.html', { 'result_list': result_list })


@login_required
def monitor_query_result_rectype(request):

    if request.method == 'POST':
        if request.POST:
            rec_type_val = str(request.POST.get('recon_type'))
            request.session['rec_type_val'] = rec_type_val
            result_list_all = NewReconUpdate.objects.filter(ReconType=str(rec_type_val)).order_by('-ReconDateTime')
        else:
            result_list_all = NewReconUpdate.objects.filter(ReconType=request.session['rec_type_val'])

    else:
        result_list_all = NewReconUpdate.objects.filter(ReconType=request.session['rec_type_val'])

    DBQuerytoCSV(result_list_all.values())

    page = request.GET.get('page', 1)

    paginator = Paginator(result_list_all, 25)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    return render(request, 'RDApp/MonitorQueryResultRecType.html', { 'result_list': result_list })



def ReconAssign(request):
    return render(request,'RDApp/ReconAssign.html',{})

# @recassgin_login_required
# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='RecAssign').exists())
# @csrf_protect
def RecAssignUpdate(request):

        # user = get_user_model()
        # print(user.objects.all()[0])

        if request.method == 'POST':

            rec_assign_form = ReconAssignForm()
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)

            if user:
                print(user)
                print(user.groups.filter(name='RecAssign').exists())
                if user.groups.filter(name='RecAssign').exists():
                    login(request,user)

                    return render(request,'RDApp/RecAssignUpdate.html',{'rec_assign_form':rec_assign_form})

                else:
                    NotPermitted = True
                    return render(request,'RDApp/RecAssignLogInPerm.html',{'NotPermitted':NotPermitted})
            else:
                print("SomeOne tried to login and failed!")
                print("username: {} and password {}".format(username,password))
                NotPermitted = False
                return render(request,'RDApp/RecAssignLogInPerm.html',{'NotPermitted':NotPermitted})

        else:
            return render(request,'RDApp/RecAssignUpdate.html',{})


def RecAssignDone(request):

        Updated = False

        if request.method == "POST":

            rec_assign_form = ReconAssignForm(data=request.POST)

            if rec_assign_form.is_valid():
                rec = rec_assign_form.save()
                # rec.userId = request.user.username
                # rec.UpdateDate = datetime.datetime.now()
                rec.save()

                Updated = True

            else:
                print(rec_assign_form.errors)

        else:
            rec_assign_form = ReconAssignForm()

        messages.info(request, 'The recon is assigned.')
        # return HttpResponseRedirect(reverse('RDApp:RecAssignDone'),{'rec_assign_form':rec_assign_form,'Updated':Updated})
        return render(request,'RDApp/RecAssignDone.html',{'rec_assign_form':rec_assign_form})
