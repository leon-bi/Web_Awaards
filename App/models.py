from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.core.validators import MaxValueValidator,MinValueValidator
from tinymce.models import HTMLField



CHOICES = (
    (1 ,1),
    (2 ,2),
    (3 ,3),
    (4 ,4),
    (5 ,5),
    (6 ,6),
    (7 ,7),
    (8 ,8),
    (9 ,9),
    (10 ,10),
    

)

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True)
    objects = models.Manager()


    class Meta:
        ordering = ['bio']


    def save_procfile(self):
        self.save()

    def get_user_projects(self):
        return self.project.all

    def __str__(self):
        return self.user.username

class Project(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="projects")
    title= models.CharField(max_length=150)
    description = HTMLField()
    project_pic = models.ImageField(null=True,upload_to="project/")
    pub_date= models.DateTimeField(auto_now_add=True)
    live_site= models.URLField(max_length=300,blank=True)
    objects = models.Manager()
    
    class Meta:
        ordering = ['title']



    def save_project(self):
        self.save()
    def get_absolute_url(self):
        return reverse("project_detail",kwargs={"pk:self.pk"})
    def __str__(self):
        return self.title

class Review(models.Model):
    project = models.ForeignKey(Project,related_name='reviews',on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
    comment = models.TextField()
    design_score = models.IntegerField(choices=CHOICES)
    usability_score = models.IntegerField(choices=CHOICES)
    content_score = models.IntegerField(choices=CHOICES)
    objects = models.Manager()


    class Meta:
        ordering = ['comment']


    def get_total(self):
        total = (design_score + usability_score + content_score)%0.33 

        return total