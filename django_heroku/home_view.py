from django.http.response import HttpResponse


from django.http import HttpResponse


def home(request):
    return HttpResponse('Olá Django Pro')