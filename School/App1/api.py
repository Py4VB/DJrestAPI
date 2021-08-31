from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *

class view1(APIView):
    def get(self, request):
        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class view2(APIView):
    def getdetail(self, rollno):
        try:
            model = Student.objects.get(rollno=rollno)
            return model
        except:
            return None
    def get(self, request, rollno):
        model = self.getdetail(rollno)
        if model==None:
            return Response("Student with Roll No " + rollno + " not found.", status.HTTP_404_NOT_FOUND)
        else:
            serializer = StudentSerializer(model)
            return Response(serializer.data, status.HTTP_200_OK)
    def put(self, request, rollno):
        model = self.getdetail(rollno)
        if model==None:
            return Response("Student with Roll No " + rollno + " not found.", status.HTTP_404_NOT_FOUND)
        else:
            serializer = StudentSerializer(model, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request, rollno):
        model = self.getdetail(rollno)
        if model==None:
            return Response("Student with Roll No " + rollno + " not found.", status.HTTP_404_NOT_FOUND)
        else:
            model.delete()
            return Response("Student with Roll No " + rollno + " deleted.", status.HTTP_200_OK)