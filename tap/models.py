from django.db import models
from django.db import connections

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    session_type = models.IntegerField()
    student = models.ForeignKey('Student', on_delete=models.RESTRICT)
    zone = models.CharField(max_length=25)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return str(self.id)
    # email = models.EmailField(max_length=200)
    # class_type = models.CharField(max_length=200)
    # date = models.DateTimeField('date published')


    class Meta:
        db_table = 'schedule'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    # class_type = models.CharField(max_length=200)
    # date = models.DateTimeField('date published')

    class Meta:
        db_table = 'students'

