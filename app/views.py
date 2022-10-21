import email
from email.message import EmailMessage
from http.client import HTTPResponse
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from app.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.


def home(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        msg = request.POST['msg']
        send_mail(
            mail,
            msg,
            name,
            ['sonuhulk8765@gmail.com'],
            fail_silently=True,
        )
        messages.success(request, 'Contact request submitted successfully.')        
    
    
    
    
    
    home = main.objects.all()
    edu = education.objects.all()
    exp = experience.objects.all()
    skilll = skill.objects.all()
    res = resume.objects.all()
    proj = projects.objects.all().reverse()
    sl = social.objects.all()
    cs = certificate.objects.all()
    ah = achievements.objects.all()
    hb = hobbies.objects.all()
    return render(request, 'index.html', context={'home': home,
                                                  'edu':edu,
                                                  'exp':exp,
                                                  'skilll':skilll,
                                                  'res':res,
                                                  'proj':proj,
                                                  'sl':sl,
                                                  'cs':cs,
                                                  'ah':ah,
                                                  'hb':hb,
                                                  })



                

    