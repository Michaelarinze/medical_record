from django.db import models

class medical_record(models.Model):
    Name = models.CharField(max_length=400)
    Sex = models.CharField(max_length=400)
    Age = models.CharField(max_length=400)
    Marital_status = models.CharField (max_length=400)
    Address =models.CharField(max_length=400)
    Medical_history = models.CharField(max_length=100000000000000000000000)
    Recomendation = models.CharField(max_length=9000000000000000000000000)
    Prescriptions =models.CharField(max_length=90000000000000000000)
    Doctors_name = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

