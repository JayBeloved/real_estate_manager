from django.db import models
from ..structure.models import Houses, Community
from ..accounts.models import User
import datetime
from django.utils import timezone
ACTIVE = 1
INACTIVE = 0

STATUS_CHOICES = (
    (INACTIVE, 'Vacated The House'),
    (ACTIVE, 'Currently Residing In The House')
)

vhl = 'VHL'
acn = 'ACN'
gen = 'GEN'
slr = 'SLR'
frt = 'FRT'
mtl = 'MTL'
ktch = 'KTCH'
oth = 'OTH'

PROPERTY_TYPES = (
    (vhl, 'Motor Vehicle'),
    (acn, 'Air Conditioner'),
    (gen, 'Generator Set'),
    (slr, 'Solar Inverter Set'),
    (frt, 'Furniture'),
    (mtl, 'Metal Works e.g Metal Cage'),
    (ktch, 'Kitchen Appliance e.g Oven'),
    (oth, 'Others, Please Specify')
)


# Create your models here.

class Residents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    house = models.ForeignKey(Houses, on_delete=models.CASCADE, to_field='housecode')
    resident_code = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    resident_email = models.EmailField(null=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    occupancy_start = models.DateField('occ_start', default=timezone.now, null=True)
    occupancy_end = models.DateField('occ_end', null=True, blank=True)
    occupancy_status = models.PositiveSmallIntegerField('Status of Residency', choices=STATUS_CHOICES, default=ACTIVE)

    def __str__(self):
        return f'Resident {self.resident_code} - {self.first_name} {self.last_name}'


class Properties(models.Model):
    resident = models.ForeignKey(Residents, on_delete=models.CASCADE, to_field='resident_code')
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES, default=vhl)
    property_code = models.CharField(max_length=30)
    property_desc = models.TextField()

    def __str__(self):
        return f'{self.property_code}'


class CommunityHeads(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, to_field='commcode')
    resident = models.ForeignKey(Residents, on_delete=models.CASCADE, to_field='resident_code')
    date_appointed = models.DateField('start_date', default=datetime.date, null=True)
    date_relieved = models.DateField('end_date', null=True)
    appointment_status = models.PositiveSmallIntegerField('Status of Appointment', choices=STATUS_CHOICES,
                                                          default=ACTIVE)

    def __str__(self):
        if self.appointment_status == 1:
            return f'Resident {self.resident} - Current Community Head For Community {self.community}'
        else:
            return f'Resident {self.resident} - Community Head for Community {self.community}' \
                   f'from {self.date_appointed} to {self.date_relieved}'
