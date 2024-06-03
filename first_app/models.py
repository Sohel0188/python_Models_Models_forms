from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField()
    
    def __str__(self):
        return f"Roll : {self.roll} -> {self.name}"
    
class Teachers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f" {self.id} - Name : {self.name}"
    