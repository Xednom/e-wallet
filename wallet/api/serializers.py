from rest_framework import serializers
from wallet.models import Cash


class CashSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Cash
        fields = "__all__"

    def get_user(self, instance):
        request = self.context.get("request")
        return '%s %s' % (request.user.first_name, request.user.last_name)

    def get_date(self, instance):
        return instance.date.strftime("%B %d, %Y")