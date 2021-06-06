from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
def student_creation(request):
    stu=Student.objects.all()
    serial=StudentSerializer(stu,many=True)
    jdata=JSONRenderer().render(serial.data)
    return HttpResponse(jdata,content_type='application/json')
