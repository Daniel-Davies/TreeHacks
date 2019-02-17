from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry', views.entry, name='entry'),
    path('upload', views.upload, name='upload'),
    path('verdict', views.verdict, name='verdict'),
    path('breakdown', views.breakdown, name='breakdown'),
    path('sendMail', views.sendMail, name='sendMail'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('forums', views.forums, name='forums'),
    path('about', views.about, name='about'),
    path('tracking', views.tracking, name='tracking'),

]