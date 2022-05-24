
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default=None)
    text = models.TextField(null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        return f"{self.text[:50]}..."

    #def save(self):
     #   if not self.id:
      #      self.image = self.compressImage(self.image)
       # super(Entry, self).save()

    def compressImage(self, image):

        img = Image.open(image).convert("RGB")
        im_io = BytesIO()

        if image.name.split('.')[1] == 'jpeg' or image.name.split('.')[1] == 'jpg':
            img.save(im_io , format='jpeg', optimize=True, quality=50)
            new_image = File(im_io, name="%s.jpeg" %image.name.split('.')[0],)
        else:
            img.save(im_io , format='png', optimize=True, quality=50)
            new_image = File(im_io, name="%s.png" %image.name.split('.')[0],)

        return new_image
