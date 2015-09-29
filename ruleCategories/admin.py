from django.contrib import admin

from ruleCategories.models import  RuleCategory

class RuleCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(RuleCategory, RuleCategoryAdmin)