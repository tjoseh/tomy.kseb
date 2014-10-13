from django.contrib import admin
from HelloWorldApp.models import *

class CounteryAdmin(admin.ModelAdmin):
    pass

class CounteryNewAdmin(admin.ModelAdmin):
    pass

class CounteryProxyAdmin(admin.ModelAdmin):
    pass

class CountryProxy(Country):
    class Meta:
        proxy = True



admin.site.register(CountryNew,CounteryNewAdmin)

admin.site.register(Country,CounteryAdmin)
admin.site.register(CountryProxy,CounteryProxyAdmin)
