from django.core.validators import RegexValidator
from django.db import models

class Customer(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    password= models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    
class ContactForm(models.Model):
    LOAN_CHOICES = [
        ('personal', 'Personal Loan'),
        ('business', 'Business Loan'),
        ('student', 'Student Loan'),
        ('emergency', 'Emergency Loan'),
        ('mortgage', 'Mortgage Loan'),
        ('smbusiness', 'Small Business Loan'),
    ]

    name = models.CharField(max_length=100)
    contact = models.CharField(
        max_length=10,
        validators= [
            RegexValidator(r'^\d{10}$', 'Enter a valid 10 digit number.')
        ]
    )

    email = models.EmailField()

    loantype = models.CharField(
    max_length=20,
    choices=LOAN_CHOICES,
    default='personal'
    )   

    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.loantype}"