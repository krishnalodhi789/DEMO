from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here
@api_view(["GET","POST"])
def student(request):
    if request.method == "POST":
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    "success":True,
                    "status":status.HTTP_201_CREATED,
                    'data':serializer.data
                }
                return Response(context)
        except Exception as error:
            context = {
                "success":True,
                "status":status.HTTP_400_BAD_REQUEST,
                'data':error
            }
            return Response(context)
        
    if request.method == "GET":
        try:
            stu = Student.objects.all()
            print(stu)
            serializer = StudentSerializer(stu,  many=True)
            context = {
                "success":True,
                "status":status.HTTP_201_CREATED,
                'data':serializer.data
            }
            return Response(context)
        except Exception as error:
            context = {
                "success":True,
                "status":status.HTTP_204_NO_CONTENT,
                'data':error
            }
            return Response(context)
        
        
@api_view(['GET','POST'])
def userview(request):
    if request.method=="POST":
       try:
            serializer = UserSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    "success":True,
                    "status":status.HTTP_201_CREATED,
                    'data':serializer.data
                }
                return Response(context)
       except Exception as error:
            context = {
                    "success":True,
                    "status":status.HTTP_204_NO_CONTENT,
                    'data':error
                }
            return Response(context)
        
    if request.method=="GET":
       try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            context = {
                "success":True,
                "status":status.HTTP_200_OK,
                'data':serializer.data
            }
            return Response(context)            
       except Exception as error:
            context = {
                    "success":True,
                    "status":status.HTTP_204_NO_CONTENT,
                    'data':error
                }
            return Response(context)


@api_view(["PUT","GET"])         
def updateStu(request,id):
    if request.method == "PUT":
        try:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu, data=request.data, partial = True)
            if serializer.is_valid():                
                serializer.save()
                context={
                    "success":True,
                    "status":status.HTTP_205_RESET_CONTENT,
                    "data":serializer.data
                }
                return Response(context)
        except Exception as error:
            context = {
                    "success":False,
                    "status":status.HTTP_404_NOT_FOUND,
                    'data':str(error)
                }
            return Response(context)