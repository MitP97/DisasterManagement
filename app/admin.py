from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SystemUsers)
admin.site.register(Families)
admin.site.register(Civilians)
admin.site.register(Shelter)
admin.site.register(Stocks)
admin.site.register(SupplierLogs)
admin.site.register(BlocksData)
admin.site.register(BlocksDict)
admin.site.register(AllocationToFamilies)
