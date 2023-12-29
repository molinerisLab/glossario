from django.contrib import admin
from .models import Teacher, Student, Course
from moxutils.admin import WithDateAndOwnerAdmin

# Register your models here.

@admin.register(Course)
class CourseAdmin(WithDateAndOwnerAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(WithDateAndOwnerAdmin):
    pass

class CourseInline(admin.TabularInline):
    model = Course.students.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [CourseInline,]

