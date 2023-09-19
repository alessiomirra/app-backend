from django.contrib import admin
from users.models import Objective 
# Register your models here.

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_filter = ["user"]

 