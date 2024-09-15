from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):    
        return reverse('post-detail', kwargs={'pk': self.pk})
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.width > 100 or img.height > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)