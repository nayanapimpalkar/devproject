from django.shortcuts import render
from .models import AccountOpeningModel
from .forms import LoanDetailsForm
# Create your views here.

def savingView(r):
    return render(r,'accounts/saving.html')




def currentView(r):
    return render(r,'accounts/current.html')



def traddingView(r):
    return render(r,'accounts/tradding.html')


def accountopeningdetails(r):
    accounts = AccountOpeningModel.objects.all()
    return render(r,'accounts/accountdetails.html',{'accounts':accounts})

def AccountView(r):
    forms = LoanDetailsForm()

    return render(r, 'accounts/accountform.html',{'forms':form})