from rest_framework import serializers
from django import forms
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

class StudentSerializer(serializers.Serializer):
    roll_no = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=20)
    mob_no = serializers.IntegerField()
    branch = serializers.CharField()
    year = serializers.IntegerField()
    sec = serializers.CharField(max_length=50)

    class StudentForm(forms.Form):
        roll_no = forms.IntegerField()
        name = forms.CharField(max_length=20)
        email = forms.EmailField()
        mob_no = forms.IntegerField()
        branch = forms.ChoiceField(choices=branch)
        year = forms.ChoiceField(choices=year)
        sec = forms.ChoiceField(choices=section)
