from django import forms
from django.contrib.auth.models import User
from RDApp.models import AccessRecord,ReconUpdate

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
    # UpdateDate = forms.DateField(widget=forms.SelectDateWidget)
    # UserId = forms.CharField(max_length=10)
    # UserEmailId = forms.EmailField()

    class Meta():
        model = ReconUpdate
        fields = ('ReconTitle','RespPers','ReconTotalCount','ReconExecutedCount','ReconDate')
        # fields = '__all__'


class QueryDateForm(forms.Form):
    query_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2030)))
