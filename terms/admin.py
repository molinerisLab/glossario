from django.contrib import admin
from reversion.admin import VersionAdmin
from terms.models import term
from moxutils.admin import export_csv_action, WithDateAndOwnerAdmin, WithDateAndOwnerAdmin_show, WithDateAndOwnerAdminStackedInline, WithDateAndOwnerAdminTabularInline, WithDateAndOwnerAdminGenericTabularInline, CsvImportForm

# Register your models here.

@admin.register(term)
class TermAdmin(VersionAdmin, WithDateAndOwnerAdmin):
    pass
