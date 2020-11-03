from django.db import models, migrations
import uuid
import os
from PIL import Image as PILImage

class Album(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=1,blank=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

