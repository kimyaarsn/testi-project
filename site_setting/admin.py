from django.contrib import admin
from .models import (
    SiteSetting,
    Banner,
    CompanyLogo,
    About,
    CallToAction,
    AbouUsFeature,
    FooterLinkBox,
    FooterLink
)


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = [
        'site_name',
        'site_url',
        'phone',
        'email',
        'is_main_setting'
    ]
    list_editable = ['is_main_setting']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['is_active']
    search_fields = ['title']


@admin.register(CompanyLogo)
class CompanyLogoAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'link'
    ]
    search_fields = ['title']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'feature_1',
        'feature_2',
        'feature_3'
    ]


@admin.register(CallToAction)
class CallToActionAdmin(admin.ModelAdmin):
    list_display = [
        'become_instructor_title',
        'student_title'
    ]


@admin.register(AbouUsFeature)
class AbouUsFeatureAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'feature_1_title',
        'feature_2_title',
        'feature_3_title',
        'feature_4_title'
    ]


@admin.register(FooterLinkBox)
class FooterLinkBoxAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [FooterLinkInline]


@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'footer_link_box',
        'url'
    ]
    list_filter = ['footer_link_box']
    search_fields = ['title']