from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('viewmore/', views.viewmore, name='viewmore'),
    path('blog/', views.blog, name='blog'),

    path('about/', views.about, name='about'),
    path('apply/', views.apply, name='apply'),
    path('careers/', views.careers, name='careers'),
    path('faq/', views.faq, name='faq'),
    path('meet/', views.meet, name='meet'),
    path('term/', views.term, name='term'),

    path('business/', views.business, name='business'),
    path('emergency/', views.emergency, name='emergency'),
    path('mortgage/', views.mortgage, name='mortgage'),
    path('personal/', views.personal, name='personal'),
    path('small/', views.small, name='small'),
    path('student/', views.student, name='student'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('Customer/', views.customerDetails, name='Customer'),
    # path('Contact/', views.contactDetails, name='Contactdet'),

]