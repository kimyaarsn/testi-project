from django.contrib import admin
from .models import (
    CourseCategory,
    CourseTag,
    Instructor,
    Course,
    CourseComment
)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active', 'is_delete']
    list_filter = ['is_active', 'is_delete']
    search_fields = ['title', 'url_title']


@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = ['caption']
    search_fields = ['caption']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'phone', 'email', 'is_active']
    list_filter = ['is_active']
    search_fields = ['full_name', 'email']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'category',
        'instructor',
        'price',
        'capacity',
        'is_active',
        'is_delete'
    ]

    list_filter = [
        'is_active',
        'is_delete',
        'category',
        'instructor'
    ]

    search_fields = [
        'title',
        'short_description',
        'description'
    ]

    filter_horizontal = [
        'course_tag',
        'suggested_courses'
    ]

    prepopulated_fields = {
        'url_title': ['title']
    }


@admin.register(CourseComment)
class CourseCommentAdmin(admin.ModelAdmin):
    list_display = [
        'course',
        'user',
        'name',
        'create_date'
    ]

    list_filter = [
        'create_date'
    ]

    search_fields = [
        'name',
        'email',
        'text'
    ]