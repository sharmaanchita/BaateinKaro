from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='avatar/', blank=True, null=True)
    info = models.TextField(blank= True, null =True)
    
    def __str__ (self):
        return str(self.user)
    
    @property
    def username(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.user.username
        return name
        
    @property
    def avatar(self):
        try:
            avatar = self.image.url
        except: 
            avatar = static("images/avatar.svg")
        return avatar
            