from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class AnonymizationSerializer(serializers.Serializer):
    data = serializers.CharField()
    technique = serializers.ChoiceField(choices=[
        'masking', 'generalization', 'k-anonymity', 'randomization',
        'aggregation', 'perturbation', 'pseudonymization', 'data_swapping',
        'synthetic_data'
    ])