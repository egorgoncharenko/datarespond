from django.db import models











class Respondent(models.Model):
    objects = models.Manager()
    okpo = models.CharField(max_length=20, verbose_name='ОКПО',unique=True)
    full_name = models.TextField(max_length=250, verbose_name='Полное наименование')
    okved = models.CharField(max_length=20, verbose_name='ОКВЭД')
    inn = models.CharField(max_length=20, verbose_name='ИНН', null=True)
    phone = models.CharField(max_length=150, verbose_name='Телефон', null=True)
    phone_double = models.CharField(max_length=150, verbose_name='Дополнительный телефон', blank=True, null=True)
    email = models.EmailField(max_length=200,  verbose_name='Email',blank=True,   null=True)
    email_double = models.EmailField(max_length=200, verbose_name="Дополнительный email", blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Респонденты'

    @classmethod
    def update_or_create_with_same_okpo(cls, okpo, **kwargs):
        respondent, created = cls.objects.update_or_create(okpo=okpo, defaults=kwargs)
        return respondent, created


