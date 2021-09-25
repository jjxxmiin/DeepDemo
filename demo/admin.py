from django.contrib import admin
from .models import Demo


class DemoAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    
    
admin.site.register(Demo, DemoAdmin)