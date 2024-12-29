from django.shortcuts import render
from django.conf import settings

class Force404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Agar 404 status kodi bo'lsa va DEBUG = True bo'lsa
        if response.status_code == 404 and settings.DEBUG:
            return render(request, '404.html', status=404)

        return response
