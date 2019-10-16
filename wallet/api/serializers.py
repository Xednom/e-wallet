from rest_framework import serializers
from wallet.models import Cash, Wallet


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Wallet
        fields = '__all__'

    def get_user(self, instance):
        request = self.context.get("request")
        return '%s %s' % (request.user.first_name, request.user.last_name)



class CashSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    wallet_user = serializers.StringRelatedField(read_only=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Cash
        fields = "__all__"

    def get_date(self, instance):
        return instance.date.strftime("%B %d, %Y")

    def get_total_amount(self, instance):
        return instance.wallet_user.balance + instance.amount_added
