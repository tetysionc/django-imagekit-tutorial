from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Post(models.Model):
    image = models.ImageField(upload_to='images')
    image_medium = ImageSpecField(source='image',
                                  processors=[Thumbnail(200, 100)],
                                  format='JPEG',
                                  options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(100, 50)],
                                 format='JPEG',
                                 options={'quality': 60})
    slug = models.SlugField(max_length=255, unique=True)
    