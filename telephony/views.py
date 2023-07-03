from rest_framework import generics

from telephony.serializers import VirtualPhoneNumberSerializer
from telephony.models import VirtualPhoneNumber


class VirtualPhoneNumberCreateListView(generics.ListCreateAPIView):
    queryset = VirtualPhoneNumber.objects.all()
    serializer_class = VirtualPhoneNumberSerializer

    def get_queryset(self):
        return VirtualPhoneNumber.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
