from django.db import models

from ..structure.models import Houses
# Create your models here.

VERIFIED = 1
UNVERIFIED = 0
CANCELLED = 2

REQUEST_STATUS = (
    (VERIFIED, 'Payment Verified'),
    (UNVERIFIED, 'Verification Pending'),
    (CANCELLED, 'Request Cancelled')
)


class AccRequest(models.Model):
    house = models.ForeignKey(Houses, on_delete=models.DO_NOTHING, to_field='housecode')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=50, default="kgera")
    status = models.PositiveSmallIntegerField('request_status', choices=REQUEST_STATUS, default=UNVERIFIED)

    def __str__(self):
        return f"Account Request From {self.last_name} {self.first_name}, for house - {self.house}"

