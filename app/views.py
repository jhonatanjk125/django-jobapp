from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

# Create your views here.
def home(request):
    jobs = JobPost.objects.all()
    context = {"jobs":jobs}
    return render(request, "app/home.html", context)


def job_detail_page(request, slug):
    if id==0:
        return redirect(reverse('jobs_home'))
    job = JobPost.objects.get(slug=slug)
    context = {"job":job}
    return render(request, "app/job_detail.html", context)



class TempClass:
    x = 5



def hello(request):
    list = ["alpha","beta"]
    temp = TempClass()
    is_authenticated = False
    context = {"name":"Django", "age":18, "first_list":list, "temp_object":temp, "authentication":is_authenticated}
    return render(request,"app/hello.html",context)