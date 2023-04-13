from django.urls import path
from. import views




urlpatterns=[
    path('',views.home, name='home'),
    path('room/',views.room,name='room'),
    path('navbar/',views.navbar,name='navbar'),
    path('main/',views.main,name='main'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup')

]
