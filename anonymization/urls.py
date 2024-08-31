from django.urls import path
from .views import anonymize_view

urlpatterns = [
    path('anonymize/', anonymize_view, name='anonymize'),
]