from django.contrib import admin
from . import models


@admin.register(models.ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'year')


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'code')


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'subject', 'author')


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('student_id', 'first_name', 'last_name', 'classroom')
	list_filter = ('classroom',)
	search_fields = ('first_name', 'last_name', 'student_id')


@admin.register(models.Attendance)
class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('student', 'date', 'status', 'subject')
	list_filter = ('status', 'date')


@admin.register(models.Mark)
class MarkAdmin(admin.ModelAdmin):
	list_display = ('student', 'subject', 'obtained', 'total', 'exam_date')
	list_filter = ('subject',)


# customize the Django admin site appearance
admin.site.site_header = "OCMS"
admin.site.site_title = "OCMS"
admin.site.index_title = "OCMS Administration"
