from django.urls import path

from . import views

urlpatterns = [
    path('api', views.json_display_demo, name='json_display_demo'),

    path('api/1', views.json_display_demo_1, name='json_display_demo_1'),

    path('api/login', views.login_request_handler, name='login_request_handler'),

    path('api/intros', views.PHGuidings_request_handler, name='PHGuidings_request_handler'),

    path('api/intro/j921jxk1lalxk2', views.PHGuiding_withname_request_handler, name='PHGuiding_withname_request_handler'),
]