from django.shortcuts import render


def get_favicon(req):
    return render(req, 'rest_framework/api.html')
