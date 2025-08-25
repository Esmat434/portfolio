from django.urls import path

from .views import (
    HomeView,ProjectListView,ProjectDetailView,AlgorithmListView,AlgorithmDetailView,ResumeView
)

app_name='home'

urlpatterns = [
    path('', HomeView.as_view(), name='home-feed'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('project/<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
    path('algorithms/', AlgorithmListView.as_view(), name='algorithm-list'),
    path('algorithm/<slug:slug>/', AlgorithmDetailView.as_view(), name='algorithm-detail'),
    path('resume/', ResumeView.as_view(), name='resume')
]