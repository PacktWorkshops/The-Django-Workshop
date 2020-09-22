from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def first_api_view(request):
    return Response({"message": "This is my first API view!!!"})
