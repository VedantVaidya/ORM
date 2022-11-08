from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="Employee"
    


class Account(models.Model):
    sallery=models.IntegerField()
    account_number=models.IntegerField()
    af=models.IntegerField()
    month=models.IntegerField(default=0)
    employe=models.ForeignKey(Employee,on_delete=models.CASCADE)

    class Meta:
        db_table="Account"

class Student(models.Model):
    Name=models.CharField(max_length=20,primary_key=True)
    City=models.CharField(max_length=20)
    Roll=models.IntegerField()

    class Meta:
        db_table="student_details"