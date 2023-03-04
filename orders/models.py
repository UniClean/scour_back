from django.db import models
from django.utils import timezone
from objects import models as object_models

import enum

class CleaningOrderType(enum.Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    COMPLAINT = 'complaint'
    OTHER = 'other'


class CleaningOrderStatus(enum.Enum):
    PLANNED = 'planned'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CONFIRMED = 'confirmed'
    OVERDUE = 'overdue'
    DECLINED = 'declined'
    OTHER = 'other'


class Order(models.Model):
    object_id = models.ForeignKey(object_models.Object, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=[(tag.name, tag.value) for tag in CleaningOrderType])
    status = models.CharField(max_length=100, choices=[(tag.name, tag.value) for tag in CleaningOrderStatus])

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    deleted_date = models.DateTimeField(blank=True, null=True)

    additional_information = models.TextField(blank=True, null=True)

    # deleted_by = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True
    # )
# Create your models here.
