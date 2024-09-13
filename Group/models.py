from django.db import models
from Person.models import Person

class Group(models.Model):
    uuid = models.UUIDField(primary_key=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    expenses_ammount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    extra = models.JSONField(default=dict, blank=True, null=True)
