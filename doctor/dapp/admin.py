from django.contrib import admin
from .models import Doctor
# Register your models here.

@admin.register((Doctor))
class doctorAdmin(admin.ModelAdmin):
    list_display=['Name','Degree','Contact','Email','Password','Image','Category']