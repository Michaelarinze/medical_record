from django.http import JsonResponse
from .models import medical_record
from .serializers import MedicalSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','PUSH'])
def medicalz(request):
    if request.method == 'GET':
        medical_records = medical_record.objects.all()
        serializer = MedicalSerializer(medical_records, many=True)
        return JsonResponse( {'medical': serializer.data})


    if request.method == 'PUSH' :
        serializer = MedicalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def medicaldetail(request,id):
    try:
         medical =medical_record.objects.get(pk=id)
    except medical.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MedicalSerializer(medical)
        return Response(serializer.data)
    
    elif request.method =="PUT":
        serailizers =MedicalSerializer(data =request.data)
        if serailizers.is_valid():
            serailizers.save()
            return Response(serailizers.data)
        return Response(serailizers.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method =="DELETE":
        medical.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
    
