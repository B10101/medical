from django.contrib import admin
from .models import Customer,Vaccine,Reservation, Contact

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vaccine)
admin.site.register(Reservation)
admin.site.register(Contact)