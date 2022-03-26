from distutils.command.upload import upload
from re import I
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Doc

class Mainview(TemplateView):
    template_name = 'tracer/main.html'

def file_upload_view(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Doc.objects.create(upload=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})