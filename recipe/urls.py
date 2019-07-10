from django.urls import path, include 

from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Recipe API')

urlpatterns = [
    path('schema/', schema_view),
]