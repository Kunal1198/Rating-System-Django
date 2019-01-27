from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('login/', views.index, name='index'),
    path('logout/', views.user_logout, name='user_logout'),
    path('proctor/', views.proctor, name="proctor"),
    path('edit_form/', views.edit_form, name="edit_form"),
    url(r'^hel/$', views.hel, name='home'),
    url(r'^api/chart/data/$', views.ChartData.as_view(), name='page2'),
    #path('student/<slug:id>/',views.AuthorUpdate.as_view(),name="student"),

    #path('studform/', views.studform, name='studform'),
]