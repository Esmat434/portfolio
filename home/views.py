from django.shortcuts import render
from django.views import View

from .models import (
    Project,Algorithm,Resume
)
# Create your views here.

class HomeView(View):
    def get(self, request):
        context = {
            'total_experience':1,
            'total_projects':Project.objects.count(),
            'total_algorithms':Algorithm.objects.count()
        }

        return render(request, 'home.html', context)

class ProjectListView(View):
    def get(self, request):
        context = {
            'projects':Project.objects.all()
        }

        return render(request,'project_list.html',context)
    
class ProjectDetailView(View):
    def get(self, request, slug):
        project = self.get_or_404(slug)

        if not project:
            return render(request, '404.html')
        
        return render(request, 'project_detail.html', {'project':project})

    def get_or_404(self,slug):
        try:
            project = Project.objects.get(slug=slug)
        except Project.DoesNotExist:
            project = None
        
        return project

class AlgorithmListView(View):
    def get(self, request):
        context = {
            'algorithms':Algorithm.objects.all()
        }

        return render(request, 'algorithm_list.html', context)

class AlgorithmDetailView(View):
    def get(self, request, slug):
        algorithm = self.get_or_404(slug)

        if not algorithm:
            return render(request,'404.html')
        
        return render(request, 'algorithm_detail.html', {'algorithm':algorithm})
    
    def get_or_404(self, slug):
        
        try:
            algorithm = Algorithm.objects.get(slug=slug)
        except Algorithm.DoesNotExist:
            algorithm=None
        
        return algorithm

class ResumeView(View):
    def get(self, request):
        context = {
            'resume': Resume.objects.all()
        }
        return render(request, 'resume.html', context)

class Custom404View(View):     
    def get(self,request, exception):
        return render(request, "404.html")