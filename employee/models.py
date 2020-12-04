from django.db import models

# Create your models here.
from django.db import models
from datetime import date
from django.forms import CheckboxSelectMultiple


# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=100, primary_key=True)
    ename = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, default="")
    dob = models.DateTimeField(blank=True, null=True)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=30)
    desig = models.CharField(max_length=100, default="")
    projects = models.CharField(max_length=500, default="")
    # pids = models.ManyToManyField(Project)
    # def get_pid_values(self):
    #     ret = ''
    #     print(self.pids.all())
    #     for e in self.pids.all():
    #          ret = ret + pids + ','
    #     return ret[:-1]
    # projects = models.CharField(max_length=100, default="") 
    # pids = models.CharField(max_length=10, default="")
    # def projectname(self):
    #     return self.projects

    #objects = models.Manager()
# class Projectss(models.Model):
#     pid = models.CharField(max_length=100)
    

class Project(models.Model):
    pid = models.CharField(max_length=100)
    pname = models.CharField(max_length=100,default="")
    pmanager = models.CharField(max_length=100, default="")
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    eids = models.ManyToManyField(Employee)
    def get_eid_values(self):
        ret = ''
        print(self.eids.all())
        for e in self.eids.all():
             ret = ret + eids + ','
        return ret[:-1]
    
