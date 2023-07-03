from django.urls import path

from telephony.views import VirtualPhoneNumberCreateListView


urlpatterns = [
    path("phonenumber/", VirtualPhoneNumberCreateListView.as_view(), name='create-list-phone-number'),    
]