from django import forms
from django.contrib.auth.models import User
from RDApp.models import AccessRecord,ReconUpdate,ReconAssignment,NewReconUpdate
from django.contrib.admin import widgets
import datetime
from django.contrib.auth import get_user_model

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm Password don't match"
            )

class ReconUpdateForm(forms.ModelForm):

    # ReconTitle = forms.CharField(max_length=100)
    # RespPerson = forms.CharField(max_length=30)
    # ReconTotalCount = forms.IntegerField()
    # ReconExecutedCount = forms.IntegerField()
    ReconDate = forms.DateField(widget=forms.SelectDateWidget)
    ReconType = forms.CharField(label='Please choose the recon type: ',widget=forms.Select(choices=[('Hourly','Hourly'),('Daily','Daily'),('Weekly','Weekly'),('Monthly','Monthly'),]))
    # ReconTime = forms.TimeField()
    # ReconDate = forms.DateTimeField(widget=forms.DateInput(attrs={'class':'timepicker'}))
    # ReconDate = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'datetimeinput'}))
    # UserId = forms.CharField(max_length=10)
    # UserEmailId = forms.EmailField()

    class Meta():
        model = ReconUpdate
        fields = ('ReconTitle','RespPers','ReconTotalCount','ReconExecutedCount','ReconDate','ReconTime','ReconType')
        # fields = '__all__'


class QueryDateForm(forms.Form):
    query_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2019, 2030)))

class QueryUserForm(forms.Form):

        user = get_user_model()
        UserChoices = list()
        for each in user.objects.all():
            UserChoices.append(('%s'%str(each),'%s'%str(each)))

        query_user = forms.CharField(widget=forms.Select(choices=UserChoices))

class QueryRecTypeForm(forms.Form):

    ReconChoices = list()
    for each in ReconAssignment.objects.values_list('UserReconType', flat=True).distinct():

        ReconChoices.append(('%s'%str(each),'%s'%str(each)))
        #ReconChoices.append(('%s'%str(each.UserReconTitle),'%s'%str(each.UserReconTitle)))

    recon_type = forms.CharField(widget=forms.Select(choices=ReconChoices))


class QueryTimePeriodForm(forms.Form):
    query_begin_date = forms.DateField(label='Choose begin date ',widget=forms.SelectDateWidget(years=range(2019, 2030)))
    query_end_date = forms.DateField(label='Choose end date ',widget=forms.SelectDateWidget(years=range(2019, 2030)))


class ReconAssignForm(forms.ModelForm):

    user = get_user_model()
    UserChoices = list()
    for each in user.objects.all():
        UserChoices.append(('%s'%str(each),'%s'%str(each)))
    # print(UserChoices)

    DefinedUser = forms.CharField(label='Please choose the recon type: ',widget=forms.Select(choices=UserChoices))
    UserFullName = forms.CharField(label='User Full Name: ',max_length=50)
    UserReconTitle = forms.CharField(label='Recon Title: ',max_length=100)
    UserReconType = forms.CharField(label='Please choose the recon type: ',widget=forms.Select(choices=[('Daily','Daily'),('Weekly','Weekly'),('Monthly','Monthly'),('Bimonthly','Bimonthly'),('BillRun','Before Each Bill Run'),('NoIntervals','Recons with no specific time period')]))
    OccuranceNum = forms.IntegerField(label='Occurance Num: ')

    # ReconDate = forms.DateField(widget=forms.SelectDateWidget)
    # ReconType = forms.CharField(label='Please choose the recon type: ',widget=forms.Select(choices=[('Hourly','Hourly'),('Daily','Daily'),('Weekly','Weekly'),('Monthly','Monthly'),]))


    class Meta():
        model = ReconAssignment
        fields = ('DefinedUser','UserFullName','UserReconTitle','UserReconType','OccuranceNum')


class NewReconUpdateForm(forms.ModelForm):

    # ReconUser = forms.CharField()
    # NewReconUpdate.objects.raw("select ReconTitle from RDApp_newreconupdate where ReconUser = 'user5'"):
    ReconChoices = list()
    # for each in ReconAssignment.objects.all():
    for each in ReconAssignment.objects.values_list('UserReconTitle', flat=True).distinct():
    #.order_by('DefinedUser').distinct('UserReconTitle'):

        # print(each)
        ReconChoices.append(('%s'%str(each),'%s'%str(each)))
        #ReconChoices.append(('%s'%str(each.UserReconTitle),'%s'%str(each.UserReconTitle)))

    # print(ReconChoices)

    ReconTitle = forms.CharField(label='Please choose the recon title: ',widget=forms.Select(choices=ReconChoices))
    ReconTotalCount = forms.IntegerField(label='Please enter recon total count: ')
    ReconExecutedCount = forms.IntegerField(label='Please enter recon executed count: ')
    ReconComments = forms.CharField(widget=forms.Textarea,required=False)
    # ReconDateTime = forms.DateTimeField()

    class Meta():
        model = NewReconUpdate
        fields = ('ReconTitle','ReconTotalCount','ReconExecutedCount','ReconComments')
