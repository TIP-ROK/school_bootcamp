from django.contrib import admin
from employee_app.models import Department, Position, Employers


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employers)
