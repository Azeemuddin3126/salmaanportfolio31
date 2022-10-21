from cProfile import label
from contextlib import nullcontext
from email import message
from enum import unique
from importlib.metadata import requires
from lzma import MODE_FAST
from pickle import NONE
from pyexpat import model
from sqlite3 import Date
from typing_extensions import Required
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.

class main(models.Model):
    img1 = models.ImageField(upload_to='imgae/', null=True, blank=True)
    heading = models.CharField(max_length=225,blank=True)
    subhead = models.TextField(max_length=500, null=True, blank=True)
    
    def __main__ (self):
        return self.heading
    
 
 
 # Education   
class education(models.Model): 
    degree = models.CharField(max_length=225)
    course = models.CharField(max_length=225)
    university = models.CharField(max_length=225)
    passout = models.CharField(max_length=225)
    cgpa = models.CharField(max_length=1000)
    
    
    def __main__(self):
        return self.degree
    
# Experience
class experience(models.Model):
    role = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    duration = models.CharField(max_length=225)
    disc = models.TextField(max_length=2223)
    
    
    def __main__(self):
        return self.degree


class certificate(models.Model):
    cname= models.CharField(max_length=224)
    pname= models.CharField(max_length=224)
    curl = models.URLField()
    descr = models.TextField()
    
    
    def __main__(self):
        return self.cname
    
class achievements(models.Model):
    aname=models.CharField(max_length=225)
    adesc = models.TextField(null=True, blank=True)
    
    def __main__(self):
        return self.aname
    
class hobbies(models.Model):
    hname = models.TextField(max_length=1000)
    
    def __main__(self):
        return self.hname
    
    
    
    




class skill(models.Model):
    skills = models.CharField(max_length=222)
    def __main__(self):
        return self.skills
    
class resume(models.Model):
    resume = models.URLField()
    
    def __main__(self):
        return self.resume
    
    
    


class projects(models.Model):
    img2 = models.ImageField(upload_to='image/',)
    projtitle = models.CharField(max_length=223)
    date = models.DateField(default=timezone.now)
    descrip = models.TextField(max_length=2224)
    projlink = models.URLField()
    
    def __main__(self):
        return self.resume
    
    
    
    
class social(models.Model):
    fb=models.URLField()
    ig=models.URLField()
    ln=models.URLField()
    gh=models.URLField()
    
    
    def __main__(self):
        return self.fb

    
        




class contact(models.Model):
    name = models.CharField(max_length=225)
    mail = models.EmailField()
    msg = models.TextField()
    
    def __str__(self):
        return self.fullname



    