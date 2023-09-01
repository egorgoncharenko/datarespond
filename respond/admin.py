from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Respondent, Phone, Email


class RespondentAdmin(ImportExportModelAdmin):
    list_display = ('okpo', 'full_name', 'okved', 'inn', 'display_phones', 'display_emails')
    search_fields = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'email')

    def display_phones(self, obj):
        phones = obj.phone.all()
        return ", ".join([phone.phone_number for phone in phones])

    display_phones.short_description = 'Телефоны'

    def display_emails(self, obj):
        emails = obj.email.all()
        return ", ".join([email.email_address for email in emails])

    display_emails.short_description = 'Emails'







class PhoneAdmin(ImportExportModelAdmin):
    list_display = ('phone_number', )


class EmailAdmin(ImportExportModelAdmin):
    list_display = ('email_address',)

admin.site.register(Respondent, RespondentAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Email, EmailAdmin)