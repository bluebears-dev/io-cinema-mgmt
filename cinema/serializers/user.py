from django.core.validators import RegexValidator
from rest_framework import serializers

from cinema.models import Client, ClientProfile
from cinema.models.user import PHONE_NUMBER_REGEX


class ClientSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=12, validators=[
        RegexValidator(
            regex=PHONE_NUMBER_REGEX
        )
    ])

    class Meta:
        model = Client
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    def create(self, validated_data):
        phone_number = validated_data.pop('phone_number', None)
        client = Client(**validated_data)
        client.is_superuser = False
        client.is_active = False
        client.save()
        ClientProfile.objects.update_or_create(user=client, phone_number=phone_number)
        return client
