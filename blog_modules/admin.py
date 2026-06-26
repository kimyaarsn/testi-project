from django.contrib import admin
from .models import (
    BlogCategory,
    BlogTag,
    BlogAuthor,
    Blog,
    BlogComment
)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'url_title',
        'is_active',
        'is_delete'
    )

    list_filter = (
        'is_active',
        'is_delete'
    )

    search_fields = (
        'title',
        'url_title'
    )

    prepopulated_fields = {
        'url_title': ('title',)
    }


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = (
        'caption',
    )

    search_fields = (
        'caption',
    )


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'is_active'
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'full_name',
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'visit_count',  # اگر این فیلد را در مدل Blog داری
        'created_date',
        'is_active',
        'is_delete'
    )

    list_filter = (
        'is_active',
        'is_delete',
        'category',
        'created_date'
    )

    search_fields = (
        'title',
        'short_description',
        'text'
    )

    prepopulated_fields = {
        'url_title': ('title',)
    }

    filter_horizontal = (
        'tags',
    )

    readonly_fields = (
        'created_date',
    )


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'blog',
        'create_date'
    )

    list_filter = (
        'create_date',
        'blog'
    )

    search_fields = (
        'name',
        'email',
        'text'
    )

    readonly_fields = (
        'create_date',
    )


from django.contrib import admin

# Register your models here.
