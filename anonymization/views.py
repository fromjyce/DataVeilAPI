from rest_framework import views, status
from rest_framework.response import Response
from .serializers import AnonymizationSerializer
from .algorithms import anonymize_data

class AnonymizeDataView(views.APIView):
    def post(self, request):
        serializer = AnonymizationSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data.get('data')
            technique = serializer.validated_data.get('technique')
            anonymized_data = anonymize_data(content, technique)
            return Response({'anonymized_data': anonymized_data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
