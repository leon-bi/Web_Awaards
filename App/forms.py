from django import forms
from .models import Project,Profile,Review
 
class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['user','bio','profile_pic']
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['author','title','description','project_pic','live_site'] 
class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review  
        fields=['project','author','comment','design_score','usability_score','content_score'] 
