from django.contrib import admin
from . models import Customer
from . models import ContactForm

admin.site.register(Customer)
admin.site.register(ContactForm)