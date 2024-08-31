from django.urls import path
from .views import AnonymizeDataView

urlpatterns = [
    path('anonymize/', AnonymizeDataView.as_view(), name='anonymize_data'),
]