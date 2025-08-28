from django.shortcuts import render
from django.http import HttpResponse
from . models import Customer
from . models import ContactForm

def home(request):
    return render(request,'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_num = request.POST.get('contact')
        email = request.POST.get('email')
        loantype = request.POST.get('loantype')
        message = request.POST.get('message')

        # Only save if all required fields are present
        if name and contact_num and email and loantype and message:
            # Validate contact number is exactly 10 digits
            if not (contact_num.isdigit() and len(contact_num) == 10):
                return render(request, 'contact.html', {'error': 'Contact number must be exactly 10 digits.'})
            try:
                rslt = ContactForm(name=name, contact=contact_num, email=email, loantype=loantype, message=message)
                rslt.save()
                return render(request, 'contact.html', {'success': True})
            except Exception as e:
                return render(request, 'contact.html', {'error': str(e)})
        else:
            return render(request, 'contact.html', {'error': 'All fields are required.'})
    return render(request, 'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')
def viewmore(request):
    return render(request,'viewmore.html')
def blog(request):
    return render(request,'blog.html')


def about(request):
    return render(request,'Pages/about.html')
def apply(request):
    return render(request,'Pages/apply.html')
def careers(request):
    return render(request,'Pages/careers.html')
def faq(request):
    return render(request,'Pages/faq.html')
def meet(request):
    return render(request,'Pages/meet.html')
def term(request):
    return render(request,'Pages/term.html')


def business(request):
    return render(request,'Services/business.html')
def emergency(request):
    return render(request,'Services/emergency.html')
def mortgage(request):
    return render(request,'Services/mortgage.html')
def personal(request):
    return render(request,'Services/personal.html')
def small(request):
    return render(request,'Services/small.html')
def student(request):
    return render(request,'Services/student.html')

def signup(request):
    return render(request,'signup.html')
def login(request):
    return render(request,'login.html')

def customerDetails(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        rslt = Customer(name = name, email = email, password = password, confirm_password = confirm_password)
        rslt.save()

    return render(request, 'login.html')