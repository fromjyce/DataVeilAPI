from django.urls import path
from .views import anonymize_data

urlpatterns = [
    path('api/anonymize/', anonymize_data, name='anonymize'),
]