from rest_framework import serializers

from telephony.models import VirtualPhoneNumber, CallLog

from telephony.funtions import is_valid_phone


class VirtualPhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualPhoneNumber
        fields = '__all__'
        read_only_fields = ['user']                     # setting user to readonly field will prevent accepting the User data from the payload

    def validate(self, attrs):
        if is_valid_phone(attrs["phone_num"]):
            return attrs
        raise serializers.ValidationError({"phone_num":"Invalid phone number."}) 


class CallLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallLog
        fields = '__all__'