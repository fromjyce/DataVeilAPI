from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

ANONYMIZATION_TECHNIQUES = (
    ('masking', 'Masking'),
    ('generalization', 'Generalization'),
    ('k-anonymity', 'K-Anonymity'),
    ('randomization', 'Randomization'),
    ('perturbation', 'Perturbation'),
    ('pseudonymization', 'Pseudonymization'),
    ('data_swapping', 'Data Swapping'),
    ('synthetic_data', 'Synthetic Data'),
)

class AnonymizationSerializer(serializers.Serializer):
    data = serializers.CharField(required=True)
    technique = serializers.ChoiceField(choices=ANONYMIZATION_TECHNIQUES, required=True)

    def validate_data(self, value):
        if not value.strip():
            raise serializers.ValidationError("Data cannot be empty or just whitespace.")
        return value