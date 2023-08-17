from django.contrib import admin
from .models import Respondent
from import_export.admin import ImportExportModelAdmin








@admin.register(Respondent)
class RespondentAdmin(ImportExportModelAdmin):
    list_display = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'phone_double', 'email', 'email_double')
    #list_filter = ('phone','full_name')
    search_fields = ('okpo', 'inn', 'full_name', 'okved', 'email', 'phone', 'email_double')





