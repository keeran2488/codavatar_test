from django.contrib.auth.models import User

from rest_framework import serializers

from telephony.models import VirtualPhoneNumber, CallLog


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class VirtualPhoneNumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = VirtualPhoneNumber
        fields = '__all__'


class CallLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = CallLog
        fields = '__all__'