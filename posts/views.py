from django.http import HttpResponse


def index(request):
    # body
    return HttpResponse("welcome to django")


def name(request):
    # body
    return HttpResponse("<h3>welcome</h3>")
