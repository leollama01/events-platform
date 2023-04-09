from datetime import datetime

from django.db import models

# Create your models here.


class User(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=120, blank=False, null=False, default=None
    )
    age = models.IntegerField(blank=False, null=False, default=None)
    country = models.CharField(
        max_length=50, blank=False, null=False, default=None
    )
    state = models.CharField(
        max_length=50, blank=False, null=False, default=None
    )
    city = models.CharField(
        max_length=50, blank=False, null=False, default=None
    )
    phone_number = models.CharField(
        max_length=16, blank=False, null=False, default=None
    )
    email = models.EmailField(
        max_length=80, blank=False, null=False, default=None
    )

    class Meta:
        db_table = 'user'
        ordering = ('id', )
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name


class Event(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=120, blank=False, null=False, default=None
    )
    date = models.DateTimeField(blank=False, null=False, default=datetime.now)
    local = models.CharField(
        max_length=60, blank=False, null=False, default=None
    )
    description = models.CharField(max_length=60, blank=True, null=True)
    free_space = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        db_table = 'event'
        ordering = ('id', )
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.name


class Payment(models.Model):

    payment_method = (
        ('CA', 'Cash'),
        ('CC', 'Credit Card'),
        ('DC', 'Debit Card'),
    )

    id = models.AutoField(primary_key=True)
    value = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False, default=0
    )
    date = models.DateTimeField(blank=False, null=False, default=datetime.now)
    status = models.BooleanField(blank=False, null=False, default=False)
    method = models.CharField(
        max_length=2, blank=False, null=False, choices=payment_method,
        default='CA'
    )

    class Meta:
        db_table = 'payment'
        ordering = ('id', )
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return self.id
