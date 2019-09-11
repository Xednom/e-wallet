from rest_framework import serializers
from users.models import CustomUser

from django_countries.serializer_fields import CountryField


class UserDisplaySerializer(serializers.ModelSerializer):
    country = CountryField()

    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name',
            'email_address', 'address', 'country',
            'state', 'zip_code'
        )
