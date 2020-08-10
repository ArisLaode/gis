from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('employee', views.employee, name='employee'),
    path('calender', views.calender, name='calender'),
    path('schedule', views.schedule, name='schedule'),
    path('learning', views.learning, name='learning'),
    path('raport', views.raport, name='raport'),
    path('exam', views.exam, name='exam'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]