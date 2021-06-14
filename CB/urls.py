from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "CB"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.homepage, name='Homepage'),
    path('authorization', views.auth, name='Authorization'),
    path('profile', views.profile, name='Profile'),
    path('college_page', views.college_page, name='CollegePage'),
    path('add_connection', views.add_connection, name='AddConnection'),
    path('ask_question', views.ask_question, name= 'AskQuestion'),
    path('answer_question', views.answer_question, name= 'AnswerQuestion'),
    path('write_review', views.write_review, name='WriteReview'),
    path('follow_college', views.follow_college, name='FollowCollege'),
]
