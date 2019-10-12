from django.shortcuts import render


def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", {"name": name})


def goodbye(request):
    name = request.GET.get("name") or "everyone"
    return render(request, "goodbye.html",
                  {"name": name, "application_name": "Bookr"}
                  )
