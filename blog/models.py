from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model): # models.Model tells django that this is a django model and needs to saved in database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # Link to another model -> Foreign Key
    title = models.CharField(max_length = 200) #Limited number of characters
    text = models.TextField() # Unlimited number of characters
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
