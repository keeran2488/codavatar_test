from rest_framework import serializers

from telephony.models import VirtualPhoneNumber, CallLog


class VirtualPhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualPhoneNumber
        fields = '__all__'
        read_only_fields = ['user']                     # setting user to readonly field will prevent accepting the User data from the payload


class CallLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallLog
        fields = '__all__'