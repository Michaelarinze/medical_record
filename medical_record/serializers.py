from rest_framework import serializers
from .models import medical_record

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = medical_record
        fields =['Name','Sex','Age','Marital_status','Address','Medical_history','Recomendation','Prescriptions','Doctors_name']