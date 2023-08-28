from django.contrib import admin
from .models import Person, addressPerson, Plan

# Register your models here.

admin.site.register(Person)
admin.site.register(Plan)
admin.site.register(addressPerson)
