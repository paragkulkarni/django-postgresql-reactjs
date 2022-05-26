from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
# Create your views here.

@api_view(['GET',])
def getAllJobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getJobById(request, pk):
    job = get_object_or_404(Job,id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNewJob(request):
    data = request.data
    job = Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer)


@api_view(['POST'])
def updateJob(request,pk):
    job = get_object_or_404(Job,id=pk)
    job.title = request.data['title']
    job.description = request.data['description']
    job.email = request.data['email']
    job.address = request.data['address']
    job.jobType = request.data['jobType']
    job.education = request.data['education']
    job.industry = request.data['industry']
    job.experience = request.data['experience']
    job.salary = request.data['salary']
    job.positions = request.data['positions']
    job.company = request.data['company']
    job.point = request.data['point']
    job.lastDate = request.data['lastDate']
    job.createdAt = request.data['createdAt']
    job.user = request.data['user']
    job.save()
    serializer = JobSerializer(job, many=False)
    return Response(serializer)

@api_view(['Delete'])
def deleteJob(request, pk):
    job = get_object_or_404(Job,id=pk)
    job.delete()
    return Response({'message':'Job is deleted successfully'}, status=status.HTTP_200_OK)