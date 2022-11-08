from django import forms
from.models import Employee,Account

class EmpForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields="__all__"

class AccForm(forms.ModelForm):

    class Meta:
        model=Account
        fields="__all__"





class EmpForm2(forms.ModelForm):

    class Meta:
        model=Employee
        fields=["name","city"]