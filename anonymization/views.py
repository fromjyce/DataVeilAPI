from rest_framework import views, status
from rest_framework.response import Response
from .serializers import DataSerializer
from .anonymization_utils import anonymize_data

class AnonymizeDataView(views.APIView):
    def post(self, request):
        content = request.data.get('content')
        technique = request.data.get('technique')
        anonymized_data = anonymize_data(content, technique)
        return Response({'anonymized_content': anonymized_data}, status=status.HTTP_200_OK)