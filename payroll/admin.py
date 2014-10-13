from django.contrib import admin
from payroll.models import *

class EmployeAdmin(admin.ModelAdmin):
    pass

class TaxAdmin(admin.ModelAdmin):
    pass

class LeaveAdmin(admin.ModelAdmin):
    pass

admin.site.register(Employe,EmployeAdmin)
admin.site.register(Tax,TaxAdmin)
admin.site.register(Leave,LeaveAdmin)
