from django.shortcuts import render
from django.views.generic import TemplateView
from site_setting.models import (SiteSetting,Banner,CompanyLogo,About,CallToAction,FooterLinkBox,AbouUsFeature)
from courses_modules.models import Course , CourseCategory , Instructor
from courses_modules.models import Course
from blog_modules.models import Blog
from account_modules.models import User


class HomeView(TemplateView):
    template_name = 'home_modules/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['site_setting'] = SiteSetting.objects.filter(
            is_main_setting=True
        ).first()

        context['banner'] = Banner.objects.filter(
            is_active=True
        ).first()

        context['company_logos'] = CompanyLogo.objects.all()

        context['about_section'] = About.objects.first()

        context['call_to_action'] = CallToAction.objects.first()

        context['instructors'] = Instructor.objects.filter(
            is_active=True
        )[:4]

        context['about'] = AbouUsFeature.objects.first()

        context['latest_courses'] = (
            Course.objects.filter(
                is_active=True,
                is_delete=False
            )
            .select_related(
                'category',
                'instructor'
            )
            .order_by('-created_date')[:6]
        )

        context['course_categories'] = CourseCategory.objects.filter(
            is_active=True,
            is_delete=False
        )[:6]

        context['latest_blogs'] = Blog.objects.filter(
            is_active=True,
            is_delete=False
        ).order_by('-created_date')[:3]

        context['students_count'] = User.objects.filter(is_active=True).count()
        context['courses_count'] = Course.objects.filter(
            is_active=True,
            is_delete=False
        ).count()

        context['blogs_count'] = Blog.objects.filter(
            is_active=True,
            is_delete=False
        ).count()

        context['instructors_count'] = Instructor.objects.filter(
            is_active=True
        ).count()

        return context


class HomeAboutView(TemplateView):
    template_name = 'home_modules/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['call_to_action'] = CallToAction.objects.first()
        context['site_setting'] = SiteSetting.objects.filter(
            is_main_setting=True
        ).first()
        context['about_section'] = About.objects.first()
        context['about'] = AbouUsFeature.objects.first()
        context['latest_blogs'] = Blog.objects.filter(
            is_active=True,
            is_delete=False
        ).order_by('-created_date')[:3]
        context['students_count'] = User.objects.filter(is_active=True).count()
        context['courses_count'] = Course.objects.filter(
            is_active=True,
            is_delete=False
        ).count()

        context['blogs_count'] = Blog.objects.filter(
            is_active=True,
            is_delete=False
        ).count()

        context['instructors_count'] = Instructor.objects.filter(
            is_active=True
        ).count()

        return context

def site_header(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request,'header_component.html',context)

def site_footer(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        var = item.links.all()
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request,'footer_component.html',context)
