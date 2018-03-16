# -*- coding: utf-8 -*-
from django.urls import path

from case_study import views

app_name = 'case_study'
urlpatterns = [
    path('get_case/<entity_id>', views.get_case_by_entity, name='get_case'),
]