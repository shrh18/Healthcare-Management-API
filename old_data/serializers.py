from rest_framework import serializers
from old_data.models import OldData


class OldDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldData
        fields = ('image',)
