from django.db import models

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STEP 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create your models here.
class Patient(models.Model):
    lastName= models.CharField(max_length=20)
    firstName= models.CharField(max_length=20)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAMES=[('hw','Height / Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName= models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue= models.CharField(max_length=20)
    measuredDateTime= models.DateTimeField(auto_now_add=True)
    patient= models.ForeignKey('Patient',on_delete=models.CASCADE)



class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    date = models.DateField(max_length=30)
    dname = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    time=models.TimeField(max_length=30,null=True)

    def __str__(self):
        return self.name
    
# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=30)
#     subject=models.CharField(max_length=20)
#     message = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name