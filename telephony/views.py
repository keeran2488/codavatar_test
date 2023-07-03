from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from telephony.serializers import VirtualPhoneNumberSerializer
from telephony.models import VirtualPhoneNumber
from telephony.pagination import StandardPagination

class VirtualPhoneNumberCreateListView(generics.ListCreateAPIView):

    queryset = VirtualPhoneNumber.objects.all()
    pagination_class = StandardPagination
    serializer_class = VirtualPhoneNumberSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return VirtualPhoneNumber.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
