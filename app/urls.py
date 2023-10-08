from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='jobs_home'),
    path('hello/', views.hello, name='hello'),
    path('jobs/<slug>', views.job_detail_page, name='jobs_detail'),
]