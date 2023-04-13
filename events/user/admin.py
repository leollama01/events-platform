from django.contrib import admin
from user.models import Event, Payment, User

# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Payment)
