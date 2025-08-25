from django.db import models
from django.utils.text import slugify
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title Projects", unique=True)
    description = models.TextField(verbose_name="Description")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Short Description")
    project_challenge = models.TextField(verbose_name='Project Challenge')
    avatar = models.ImageField(upload_to='projects/', verbose_name="Main Picture")
    slug = models.SlugField(unique=True)

    github_link = models.URLField(max_length=500, verbose_name="Github Link")
    demo_link = models.URLField(max_length=500, blank=True, null=True, verbose_name="Demo Link")
    
    technologies_used = models.CharField(max_length=500, blank=True, verbose_name="Technologies Used")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_at")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
class Algorithm(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title Algorithm', unique=True)
    description = models.TextField(verbose_name='Full Description')
    short_description = models.CharField(max_length=500, verbose_name='Short Description')
    algorithm_challenge = models.TextField(verbose_name='Algorithm Challenge')
    avatar = models.ImageField(upload_to='algorithms/image/', blank=True, null=True, verbose_name='Avatar')
    slug = models.SlugField(unique=True)

    time_complexity = models.CharField(max_length=50, verbose_name='Time Complexity')
    space_complexity = models.CharField(max_length=50, verbose_name='Space Complexity')

    github_link = models.URLField(max_length=500, verbose_name='Github Link')

    technologies_used = models.CharField(max_length=500, blank=True, verbose_name="Technologies Used")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

    class Meta:
        verbose_name = 'Algorithm'
        verbose_name_plural = 'Algorithms'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Title {self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
        