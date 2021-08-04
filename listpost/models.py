from django.db import models

# Create your models here.


class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()



UNITS = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5以上'),('無','無'))
COMPANY = (('docomo','docomo'),('au','au'),('softbank','softbank'),('UQ','UQ'),('Ymobile','Ymobile'),('無','無'))
BB = (('docomo光','docomo光'),('auひかり・固定代替','auひかり・固定代替'),('softbank光・Air','softbank光・Air'),('nifty光','nifty光'),('NURO光','NURO光'),('その他','その他'),('無','無'))
LAYAWAY = (('済','済'),('未','未'))

class ListModel(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='お客様名'
        )
    tel = models.CharField(
        max_length=12,
        verbose_name='ご連絡先')
    units = models.CharField(
        max_length = 50,
        verbose_name = '希望台数',
        choices = UNITS
    )
    company = models.CharField(
        max_length = 50,
        verbose_name ='希望キャリア',
        choices = COMPANY
    )
    bb = models.CharField(
        max_length = 50,
        verbose_name ='インターネット',
        choices = BB
    )
    layaway = models.CharField(
        max_length = 50,
        verbose_name ='取り置き',
        choices = LAYAWAY
    )
    remarks = models.TextField(
        max_length=300,
        verbose_name ='備考'
        )
    postdate = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        