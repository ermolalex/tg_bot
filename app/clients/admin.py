from django.contrib import admin

from .models import Client, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ['name']


@admin.display(description='ФИО')
def fio(obj):
    return f"{obj.fio}"

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    #ordering = ['company_name']
    list_display = ['company_name', 'fio', 'phone_number', 'tg_id', 'zulip_channel_id']

    def company_name(self, obj):
        if obj.company:
            return obj.company.name
        return ""

    def fio(self, obj):
        return obj.fio

    company_name.admin_order_field = 'company'
    fio.admin_order_field = 'first_name'
