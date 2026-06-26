from django.shortcuts import render, redirect
from django.views import View
from site_setting.models import SiteSetting
from .form import ContactModelForm


class ContactView(View):

    def get(self, request):
        contact_form = ContactModelForm()
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()

        return render(request, 'contact_modules/contact.html', {
            'contact_form': contact_form,
            'site_setting': site_setting,
        })

    def post(self, request):
        contact_form = ContactModelForm(request.POST)
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()

        if contact_form.is_valid():
            contact_form.save()
            return redirect('index')

        return render(request, 'contact_modules/contact.html', {
            'contact_form': contact_form,
            'site_setting': site_setting,
        })