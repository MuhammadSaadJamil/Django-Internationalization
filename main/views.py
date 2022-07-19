import time

from django.conf import settings
from django.shortcuts import render
from django.utils.timezone import now
from django.utils.translation import gettext as _

from forms import TestForm
from main.models import Test


def home(request):
    data = {
        "title": _("Home"),
        "Heading": _("Welcome to Home"),
        "user": request.COOKIES.get('User', "New User"),
        'location': request.session.get('location', "404 Location")
    }

    response = render(request, 'index.html', data)
    # response.set_cookie('User', "Dev MAC", max_age=3600)
    request.session['location'] = 'Islamabad'
    # request.session.clear()

    return response


def create_test(request):
    if request.POST:
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'form.html', {'form': TestForm()})


def update_test(request, id):
    test = Test.objects.get(id=id)
    if request.POST:
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            test = form.save()
    return render(request, 'form.html', {'form': TestForm(instance=test)})