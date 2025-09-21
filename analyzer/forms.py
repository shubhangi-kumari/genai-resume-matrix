from django import forms
from .models import ResumeUpload

class ResumeForm(forms.ModelForm):
    job_title = forms.CharField(max_length=200, required=False, help_text="Optional: Target job for skill comparison")
    
    class Meta:
        model = ResumeUpload
        fields = ['resume_file']