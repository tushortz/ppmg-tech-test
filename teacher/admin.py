from django.contrib import admin
from teacher.models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_no']
    ordering = ['first_name', 'last_name']