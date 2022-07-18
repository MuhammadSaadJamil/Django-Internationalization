from django.conf import settings
from django.shortcuts import render
from django.utils.timezone import now
from django.utils.translation import gettext as _


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
