from django.contrib import admin

from .models import Employee, Project

admin.site.register(Employee)
# admin.site.register(Projectss)
admin.site.register(Project)