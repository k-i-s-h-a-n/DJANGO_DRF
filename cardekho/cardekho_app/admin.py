from django.contrib import admin

from .models import carList,showroomList

# Register your models here.
admin.site.register(carList)
admin.site.register(showroomList)