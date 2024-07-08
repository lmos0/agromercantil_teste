from django.contrib import admin
from .models import Commodity, CommodityData

# Register your models here.

admin.site.register(Commodity)
admin.site.register(CommodityData)