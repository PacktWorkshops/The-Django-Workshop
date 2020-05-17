from django.http import HttpResponse


def welcome_view(request):
    message = "<html><h1>Welcome to Bookr!</h1></html>"
    return HttpResponse(message)