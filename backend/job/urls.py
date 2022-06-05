from django.urls import URLPattern, path
from . import views


urlpatterns=[
    path('jobs/', views.getAllJobs, name='jobs'),
    path('jobs/new/', views.createNewJob, name='new_job'),
    path('job/<str:pk>/', views.getJobById, name='job_by_id'),
    path('job/<str:pk>/update/', views.updateJob, name='job_update'),
    path('job/<str:pk>/delete/', views.deleteJob, name='job_delete'),
    path('stats/<str:topic>/', views.getTopicStats, name='get_topic_stats'),
]