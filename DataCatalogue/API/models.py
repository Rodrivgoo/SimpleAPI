from django.db import models

# Create your models here.

class JSONData(models.Model):
    file = models.FileField(upload_to='json_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)