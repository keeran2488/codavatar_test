from django.contrib import admin

from telephony.models import (
    VirtualPhoneNumber, 
    CallLog
)


admin.site.register(VirtualPhoneNumber)
admin.site.register(CallLog)

