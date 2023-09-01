from django.urls import path

from . import views

app_name = 'streakchat'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('home/', views.home_page, name='home'),
    path('home/addcontact/', views.add_contact_page, name='add_contact'),
    path('chat/<str:room_name>/', views.room_page, name='room')
]