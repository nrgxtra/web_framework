from django.shortcuts import render


def landing_page(request):
    return render(request, 'templates/landing_page.html')


