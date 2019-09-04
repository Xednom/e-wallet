from rest_framework import serializers
from wallet.models import Cash


class CashSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    card_details = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cash
        fields = "__all__"

    def get_date(self, instance):
        return instance.date.strftime("%B %d, %Y")