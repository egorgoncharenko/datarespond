from django.db import models





class Email(models.Model):
    address = models.EmailField(max_length=100, verbose_name='Адрес почты ', blank=True, null=True)

    def __str__(self):
        return self.address
    class Meta:
        verbose_name_plural = 'Электронная почта'


class Phone(models.Model):
    address = models.TextField(max_length=100, verbose_name='Номер телефона ', blank=True, null=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = 'Телефон'



class Respondent(models.Model):
    objects = models.Manager()
    okpo = models.CharField(max_length=20, verbose_name='ОКПО', unique=True)
    full_name = models.TextField(max_length=250, verbose_name='Полное наименование')
    okved = models.CharField(max_length=20, verbose_name='ОКВЭД')
    inn = models.CharField(max_length=20, verbose_name='ИНН', null=True)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, verbose_name='Телефон', related_name='respondents', null=True)
    email = models.ForeignKey(Email,  on_delete=models.CASCADE,  verbose_name='Email',  related_name='respondents', null=True)

    class Meta:
        verbose_name_plural = 'Респонденты'

