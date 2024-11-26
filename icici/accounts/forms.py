from django import forms
from .models import AccountOpeningModel


class LoanDetailsForm(forms.ModelForm):
    class Meta:
        model = AccountOpeningModel
        fileds = "__all__"