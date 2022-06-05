from itertools import count
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Job
from django.db.models import Count, Min, Max, Avg, Aggregate
from .serializers import JobSerializer
from .filters import JobsFilter
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET',])
def getAllJobs(request):
    filterset = JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    # jobs = Job.objects.all()
    resPerPage = 3
    count = filterset.qs.count()
    paginator = PageNumberPagination()
    paginator.page_size = resPerPage
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = JobSerializer(queryset, many=True)
    return Response({
        'count': count,
        'resPerPage': resPerPage,
        'jobs':serializer.data})

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

@api_view(['DELETE'])
def deleteJob(request, pk):
    job = get_object_or_404(Job,id=pk)
    job.delete()
    return Response({'message':'Job is deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getTopicStats(request, topic):
    args = {'title__icontains':topic}
    jobs = Job.objects.filter(**args)
    print("length - ", len(jobs))

    if len(jobs)==0:
        return Response({'massage': 'Not stats find for {topic}'.format(topic=topic )})

    stats = jobs.aggregate(
        total_jobs = Count('title'),
        avg_positions = Avg('positions'),
        avg_salary = Avg('salary'),
        min_salary = Min('salary'),
        max_salary=Max('salary')
    )

    return Response(stats)