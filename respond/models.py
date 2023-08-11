from django.db import models



# class Phone(models.Model):
#
#     phone = models.IntegerField(  verbose_name='Телефон', blank=True)
#
#     def __str__(self):
#         return self.phone
#
#     class Meta:
#         verbose_name_plural = 'Телефоны'

class Respondent(models.Model):
    objects = models.Manager()
    okpo = models.CharField(max_length=20, verbose_name='ОКПО', unique=True)
    full_name = models.CharField(max_length=200, verbose_name='Полное наименование')
    okved = models.CharField(max_length=20, verbose_name='ОКВЭД')
    inn = models.CharField(max_length=20, verbose_name='ИНН', null=True)
    phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email', blank=True, null=False)





    class Meta:
        verbose_name_plural = 'Респонденты'


