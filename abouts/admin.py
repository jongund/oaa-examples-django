from django.contrib import admin
from abouts.models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_slug', 'title')

admin.site.register(About, AboutAdmin)

