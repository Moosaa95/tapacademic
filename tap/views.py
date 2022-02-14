from .serializers import ScheduleSerializer, StudentsSerializer
from rest_framework import generics
from .models import Schedule, Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET', 'POST'])
def schedule_list(request):
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        schedules = ScheduleSerializer(data=request.data)
        if schedules.is_valid():
            schedules.save()
            return Response(schedules.data, status=status.HTTP_201_CREATED)
        return Response(schedules.errors, status=status.HTTP_400_BAD_REQUEST)


#get teacher id
#use teacher id to get link of schedule
        


