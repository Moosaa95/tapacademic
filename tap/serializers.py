from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'session_type','zone', 'student', 'date', 'time')
    

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'fullname',)