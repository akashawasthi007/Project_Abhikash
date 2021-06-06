from django.db import models

# Create your models here.

branch = (
    ('CS','Computer Science'),
    ('ME','Mechanical Engineering'),
    ('CE','Civil Engineering'),
    ('IT','Information Technology'),
    ('EN','Electrical Engineering'),
)
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

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mob_no = models.IntegerField()
    branch = models.CharField(max_length=2, choices=branch, default='CS')
    year = models.IntegerField(choices=year, default=1)
    sec = models.CharField(max_length=50, choices=section, default='A')
    def __str__(self):
        return self.name
