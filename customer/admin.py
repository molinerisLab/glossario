from django.contrib import admin
from moxutils.admin import export_csv_action, WithDateAndOwnerAdmin, WithDateAndOwnerAdmin_show, WithDateAndOwnerAdminStackedInline, WithDateAndOwnerAdminTabularInline
from .models import Customer, Group
from .forms import CustomerForm


class MyAdmin(WithDateAndOwnerAdmin_show):
    pass

class CustomersInGroupInline(WithDateAndOwnerAdminTabularInline):
    model = Customer
    verbose_name = "Customers in group"
    verbose_name_plural = "Customers in group"
    def has_add_permission(self, request, o):
        return False

@admin.register(Group)
class GroupAdmin(MyAdmin):
    inlines = (CustomersInGroupInline, ProjectsInGroupInline)

@admin.register(Customer)
class CustomerAdmin(MyAdmin):
    form = CustomerForm
    list_display=('__str__','owner','email','name','surname',)
    list_editable=("email","name","surname",)
    search_fields=('surname','name','email')
    readonly_fields = ('user','owner')
    list_per_page=10
