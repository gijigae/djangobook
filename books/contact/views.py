from django.shortcuts import render
from books.contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def contact(request):
    form = ContactForm(
        initial={'subject': 'I love your site!'}
    )
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@choimirai.com'),
                ['sangmin@choimirai.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')

    return render(request, 'contact_form.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')


def current_time(request):
    return render(request, 'current_time.html')


def current_time2(request):
    return render(request, 'current_time.html')
