from django.urls import path
from . import views

urlpatterns = [
    path('studenthome/',views.studenthome,name="studenthome"),
    path('studentlogout/',views.studentlogout,name='studentlogout'),
    path('studentresponse/',views.response,name='response'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('postquestion/',views.postquestion,name='postquestion'),
    path('postanswer/<qid>',views.postanswer,name='postanswer'),
    path('postans/',views.postans,name='postans'),
    path('viewanswer/<qid>',views.viewanswer,name='viewanswer'),
    path('viwprofile',views.viewprofile,name='viewprofile'),
    path('viewstudymaterail',views.viewsmat,name='viewsmat'),
     path('viewassignment',views.viewassign,name='viewassign'),
]

