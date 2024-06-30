from django.contrib import admin

from .models import carList,showroomList,Review

# Register your models here.
admin.site.register(carList)
admin.site.register(showroomList)
admin.site.register(Review)