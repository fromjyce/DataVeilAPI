from django.urls import path
from .views import AnonymizeDataView

urlpatterns = [
    path('', AnonymizeDataView.as_view(), name='anonymize-data'),
]