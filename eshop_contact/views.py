from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactUs
from eshop_settings.models import FooterSetting


def contact_page(request):
    contact_form = ContactUs(request.POST or None)

    if contact_form.is_valid():
        fullname = contact_form.cleaned_data.get('fullname')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')

        Contact.objects.create(fullname=fullname, email=email, subject=subject, text=text, is_read=False)

        contact_form = ContactUs()
        return redirect('/contact-us')

    footer_setting = FooterSetting.objects.first()

    context = {
        'title': 'contact-us',
        'contact_form': contact_form,
        'footer': footer_setting
    }

    return render(request, 'contact-us/Contact-us.html', context)
