from django.db import models

class Respondent(models.Model):
    objects = models.Manager()
    okpo = models.CharField(max_length=20, verbose_name='ОКПО', unique=True)
    full_name = models.TextField(max_length=250, verbose_name='Полное наименование')
    okved = models.CharField(max_length=20, verbose_name='ОКВЭД')
    inn = models.CharField(max_length=20, verbose_name='ИНН', null=True)
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE, verbose_name='Телефон', related_name='respondent', null=False, blank=True)
    email = models.ForeignKey('Email', on_delete=models.CASCADE, verbose_name='Email', related_name='respondent', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Респонденты'

class Phone(models.Model):
    phone_number = models.CharField(max_length=150, verbose_name='Телефон', null=False, blank=True)



    class Meta:
        verbose_name_plural = 'Телефоны'

class Email(models.Model):
    email_address = models.EmailField(max_length=200, verbose_name='Email')



    class Meta:
        verbose_name_plural = 'Электронный адрес'



    #
    # @classmethod
    # def update_or_create_with_same_okpo(cls, okpo, **kwargs):
    #     respondent, created = cls.objects.update_or_create(okpo=okpo, defaults=kwargs)
    #     return respondent, created

