from django.contrib import admin
from teacher.models import Teacher, Subject

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_no']
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'subjects_taught']
    list_filter = ['subjects_taught']
    filter_horizontal = ['subjects_taught']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']