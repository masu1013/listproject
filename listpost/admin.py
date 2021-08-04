from django.contrib import admin
from .models import SampleModel, ListModel

# Register your models here.

admin.site.register(SampleModel)
admin.site.register(ListModel)