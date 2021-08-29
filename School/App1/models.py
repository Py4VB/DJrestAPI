from django.db import models

#Creating a db table
class Student(models.Model):
    rollno = models.CharField(max_length=3, unique=True)
    name = models.TextField()
    
    def uploaddoc(self, filename):
        return './documents/' + filename

    documents = models.FileField(upload_to=uploaddoc, null=True, blank=True)