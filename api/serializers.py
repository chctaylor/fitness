from rest_framework import serializers
from fitness.models import BodyComposition


class BodyCompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyComposition
        fields = '__all__'