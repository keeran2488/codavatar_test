from django.db import models

from account.models import User


class VirtualPhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=14, verbose_name="Phone number", unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.phone_num}"
    

class CallLog(models.Model):
    phone_num = models.ForeignKey(VirtualPhoneNumber, on_delete=models.CASCADE, verbose_name="Phone number")
    duration = models.DurationField(default=0)
    recipient_num = models.CharField(max_length=14, verbose_name="Recipient number", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_num.phone_num} -> {self.recipient_num} - {self.duration}"


