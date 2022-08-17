from django.contrib import admin
from .models import *
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)
    readonly_fields = ('user',)
    exclude = ('favorites', 'created_at', 'updated_at',)
    date_hierarchy = 'created_at'
    list_display = ('user', 'role', 'birth', 'positionsList',  'officeList',)
    list_display_links = ('user', 'role',)
    empty_value_display = '----'
    list_filter = ('user__is_active', 'role')
    fieldsets = (
        ('Usuário', {
            'fields': ('user', 'birthday', 'image')
        }),
        ('Função', {
            'fields': ('role',)
        }),
        ('Extras', {
            'fields': ('positions','office')
        }),
    )
 
    def positionsList(self, obj):
        return [i.name for i in obj.positions.all()]
    def officeList(self, obj):
        return [i.name for i in obj.office.all()]
 
    def birth(self, obj):
        if obj.birthday:
            return obj.birthday.strftime("%d/%m/%Y")
    birth.empty_value_display = '___/___/_____'
    class Media:
        css = {
            "all": ("css/custom.css",)
        }
        js = ("js/custom.js",)