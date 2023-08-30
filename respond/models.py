from django.db import models

class Respondent(models.Model):
    objects = models.Manager()
    okpo = models.CharField(max_length=200, verbose_name='ОКПО')
    full_name = models.TextField(max_length=200, verbose_name='Полное наименование')
    okved = models.CharField(max_length=50, verbose_name='ОКВЭД')
    inn = models.CharField(max_length=50, verbose_name='ИНН', null=True)
    phone = models.ManyToManyField('Phone',   verbose_name='Телефон', related_name='respondent')
    email = models.ManyToManyField('Email',  verbose_name='Email', related_name='respondent')



    class Meta:
        verbose_name_plural = 'Респонденты'



class Phone(models.Model):
    phone_number = models.TextField(max_length=150, verbose_name='Телефон')
    okpo = models.CharField(max_length=200, verbose_name='ОКПО')

    def __str__(self):
          return  self.phone_number


    class Meta:
        verbose_name_plural = 'Телефоны'





class Email(models.Model):
    email_address = models.EmailField(max_length=200, verbose_name='Email')

    def __str__(self):
          return  self.email_address


    class Meta:
        verbose_name_plural = 'Электронный адрес'