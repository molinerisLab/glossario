from django.contrib import admin
from reversion.admin import VersionAdmin
from terms.models import Term, Subject, Topic
from moxutils.admin import export_csv_action, WithDateAndOwnerAdmin, WithDateAndOwnerAdmin_show, WithDateAndOwnerAdminStackedInline, WithDateAndOwnerAdminTabularInline, WithDateAndOwnerAdminGenericTabularInline, CsvImportForm

# Register your models here.

@admin.register(Term)
class TermAdmin(VersionAdmin, WithDateAndOwnerAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(VersionAdmin, WithDateAndOwnerAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(VersionAdmin, WithDateAndOwnerAdmin):
    pass
