from django.shortcuts import render
from RDApp.forms import UserForm,ReconUpdateForm,QueryDateForm
from django import forms
import datetime
from RDApp.models import ReconUpdate

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from django_tables2 import RequestConfig
from RDApp.tables import ResultTable

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
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('RDApp:RecUpdated'))    #reverse('admin:index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("SomeOne tried to login and failed!")
            print("username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied!!")
    else:
        return render(request,'RDApp/UpdateLoggedIn.html',{})


@login_required
def RecUpdated(request):

    Updated = False

    if request.method == "POST":

        # request_dict = dict(request.POST)
        # print(type(dict(request.POST)))
        # dt_string = str(datetime.datetime.now()).replace(' ','-')
        # print(dt_string)
        # custom_dict = {'userId':request.user.username,'UpdateDate':datetime.date(int(dt_string.split('-')[0]),int(dt_string.split('-')[1]),int(dt_string.split('-')[2]))}
        # custom_dict = {'userId':request.user.username,'UpdateDate_day':['%s'%dt_string.split("-")[2]],
        # 'UpdateDate_month':['%s'%dt_string.split("-")[1]],'UpdateDate_year':['%s'%dt_string.split("-")[0]]}
        # data_dict = {}
        # data_dict.update(request_dict)
        # data_dict.update(custom_dict)
        rec_update_form = ReconUpdateForm(data=request.POST)

        if rec_update_form.is_valid():
            rec = rec_update_form.save()
            # rec.userId = request.user.username
            # rec.UpdateDate = datetime.datetime.now()
            rec.save()

            Updated = True

        else:
            print(rec_update_form.errors)

    else:
        rec_update_form = ReconUpdateForm()

    return render(request,'RDApp/RecUpdated.html',{'rec_update_form':rec_update_form,
                                'Updated':Updated})


def monitor_user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('RDApp:MonitorQuery'))    #reverse('admin:index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("SomeOne tried to login into monitoring portal and failed!")
            print("username: {} and password {}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied!!")
    else:
        return render(request,'RDApp/MonitorQuery.html',{'query_date_form':QueryDateForm()})


@login_required
def monitor_query_result(request):

    if request.method == 'POST':
        if request.POST:
            rec_date_val = str(datetime.date(int(request.POST.get('query_date_year')),int(request.POST.get('query_date_month')),int(request.POST.get('query_date_day'))))
            request.session['rec_date_val'] = rec_date_val
            result_list_all = ReconUpdate.objects.filter(ReconDate__gt=rec_date_val)
        else:
            result_list_all = ReconUpdate.objects.filter(ReconDate__gt=request.session['rec_date_val'])

    else:
        result_list_all = ReconUpdate.objects.filter(ReconDate__gt=request.session['rec_date_val'])

    page = request.GET.get('page', 1)

    paginator = Paginator(result_list_all, 10)
    try:
        result_list = paginator.page(page)
    except PageNotAnInteger:
        result_list = paginator.page(1)
    except EmptyPage:
        result_list = paginator.page(paginator.num_pages)

    return render(request, 'RDApp/MonitorQueryResult.html', { 'result_list': result_list })

    # return render(request, 'RDApp/MonitorQueryResult.html', {'result_list': result_list_all})
