from django.contrib import admin
from .models import Respondent
from import_export.admin import ImportExportModelAdmin







@admin.register(Respondent)
class RespondentAdmin(ImportExportModelAdmin):
    list_display = ('okpo', 'full_name', 'okved', 'inn',   'email', 'phone')
    search_fields = ('okpo', 'inn', 'full_name', 'okved', 'phone')




#@admin.register(Phone)
#class RespondentAdmin(ImportExportModelAdmin):
    #pass