from django.db import models

# Create your models here.

class employes(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


    def __str__(self):
            return self.summary



class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=50)
    employee_department = models.CharField(max_length=50)


    def __str__(self):
        return self.summary
