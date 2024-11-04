from rest_framework import serializers
from v1.models import *


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionAPI
        fields = ['transaction_id','name','phone','email','amount','transaction_date','status']
        read_only_fields = ['transaction_id','status']