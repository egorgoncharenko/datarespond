from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Respondent

class RespondentResource(resources.ModelResource):
    class Meta:
        model = Respondent

class RespondentAdmin(ImportExportModelAdmin):
    resource_class = RespondentResource
    list_display = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'phone_double', 'email', 'email_double')
    search_fields = ('okpo', 'full_name', 'okved', 'inn', 'phone', 'phone_double', 'email', 'email_double')

    def import_data(self, dataset, dry_run=False, **kwargs):
        # Импорт данных из файла
        result = super().import_data(dataset, dry_run, **kwargs)

        if not dry_run:
            for row in dataset.dict:
                okpo = row['okpo']
                email = row['email']
                phone = row['phone']

                try:
                    # Попытка получить существующего респондента с указанным okpo
                    respondent = Respondent.objects.get(okpo=okpo)

                    # Обновление полей email и phone у найденного респондента
                    respondent.email = email
                    respondent.phone = phone
                    respondent.save()
                except Respondent.DoesNotExist:
                    # Если респондент с указанным okpo не найден, продолжить обработку следующей записи
                    pass

            self.message_user(request, "Successfully updated {result.totals['updated']} respondents.")

        return result

admin.site.register(Respondent, RespondentAdmin)







