from django.shortcuts import render
from uploadfiles.forms import UploadFileForm, UploadForm

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            saved_object = upload_form.instance
            context = { 'upload_form':upload_form, 'saved_object':saved_object}
            return render(request, 'uploadfiles/upload_image.html', context)
    else: 
        upload_form = UploadForm()
    context = {'upload_form':upload_form}
    return render(request, 'uploadfiles/upload_image.html', context)


def upload_file(request):
    if request.method == 'POST':
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save()
            saved_object = upload_form.instance
            context = { 'upload_form':upload_form, 'saved_object':saved_object}
            return render(request, 'uploadfiles/upload_file.html', context)
    else: 
        upload_form = UploadFileForm()
    context = {'upload_form':upload_form}
    return render(request, 'uploadfiles/upload_file.html', context)