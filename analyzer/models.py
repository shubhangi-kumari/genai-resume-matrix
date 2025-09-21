from django.db import models

# Create your models here.
from django.db import models

class ResumeUpload(models.Model):
    resume_file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
