from django.urls import path
from .import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('viewstudent/',views.viewstudent,name='viewstudent'),
    path('viewenquiry/',views.viewenquiry,name='viewenquiry'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('viewcomplain/',views.viewcomplain,name='viewcomplain'),
    path('uploadmaterial/',views.uploadmaterial,name='uploadmaterial'),
    path('news/',views.addnews,name='addnews'),
    path('delnews/<nid>',views.delnews,name='delnews'),

]