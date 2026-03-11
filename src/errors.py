from django.shortcuts import render


def http404(request, exception):

    return render(request, "errors/404.html", status=404)






