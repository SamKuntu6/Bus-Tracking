from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'town', 'address', 'has_profile')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stud_name', 'parent_name', 'relationship', 'classroom', 'parent_phone', 'is_active')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'created', 'updated', 'name', 'type')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employee, EmployeeAdmin)
