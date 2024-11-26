from django.contrib import admin
from .models import AccountOpeningModel
# Register your models here.


class AccountOpeningAdmin(admin.ModelAdmin):
    list_display = ['refid','name','age','email','DOR','mobile','count']


admin.site.register(AccountOpeningModel,AccountOpeningAdmin)

