from django.db import models
from django.contrib.auth.models import User
# Create your models here.

branch = (
    ('CS','Computer Science'),
    ('ME','Mechanical Engineering'),
    ('CE','Civil Engineering'),
    ('IT','Information Technology'),
    ('EN','Electrical Engineering'),
)
# leader ENDVR20217895685215
section = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
)
year = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)


class student(models.Model):
    #user = OneToOneField(User,on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    mob_no = models.IntegerField()
    branch = models.CharField(max_length=2, choices=branch, default='CS')
    year = models.IntegerField(choices=year, default=1)
    sec = models.CharField(max_length=50, choices=section, default='A')
    def __str__(self):
        return self.name
