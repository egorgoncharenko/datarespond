from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Respondent,Phone, Email


class RespondentAdmin(ImportExportModelAdmin):
    list_display = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'email')
    search_fields = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'email')

class PhoneAdmin(ImportExportModelAdmin):
    list_display = ('phone_number',)

class EmailAdmin(ImportExportModelAdmin):
    list_display = ('email_address',)

admin.site.register(Respondent, RespondentAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Email, EmailAdmin)