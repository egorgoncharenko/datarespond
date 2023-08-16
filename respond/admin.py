from django.contrib import admin
from .models import Respondent, Email, Phone
from import_export.admin import ImportExportModelAdmin








@admin.register(Respondent)
class RespondentAdmin(ImportExportModelAdmin):
    list_display = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'email')
    #list_filter = ('phone','full_name')
    search_fields = ('okpo', 'inn', 'full_name', 'okved')




@admin.register(Email)
class EmailAdmin(ImportExportModelAdmin):
  pass


@admin.register(Phone)
class PhoneAdmin(ImportExportModelAdmin):
  pass