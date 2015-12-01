from django.contrib import admin

from examples.models import  Example

class ExampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter  = ('status',)
    
admin.site.register(Example, ExampleAdmin)