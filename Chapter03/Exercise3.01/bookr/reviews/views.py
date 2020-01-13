from django.http import HttpResponse


def hello_world(request):
    message = "<html><h1>Hello world.</h1></html>"
    return HttpResponse(message)