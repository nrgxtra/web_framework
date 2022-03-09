from django.shortcuts import render, redirect

from phones_media_files.phones.forms import CreatePhone
from phones_media_files.phones.models import Phone, PhoneImage


def index(request):
    phones = Phone.objects.all()
    for phone in phones:
        phone.selected_image = phone.phoneimage_set.filter(is_selected=True).first()
    context = {
        'phones': phones,
    }
    return render(request, 'index.html', context)


def add_phone(request):
    if request.method == 'POST':
        form = CreatePhone(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {
        'form': CreatePhone(),
    }

    return render(request, 'create.html', context)


# def add_image(request):
#     if request.method == 'POST':
#         form = AddImage(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {
#         'form': AddImage(),
#     }
#     return render(request, 'add_image.html', context)

