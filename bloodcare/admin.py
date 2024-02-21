from django.contrib import admin
from .models import *

# # Register your models here.
@admin.register(donordetails)
class DonorDetailsAdmin(admin.ModelAdmin):
    list_display=['name','prov_no','district','city','dob','gender','phoneno']


admin.site.register(requestdetails)
# admin.site.register(reward)
admin.site.register(imagefilled)
