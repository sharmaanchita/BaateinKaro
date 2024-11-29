from django.db import models
from django.contrib.auth.models import User
import shortuuid
# Create your models here.
class ChatGroup(models.Model):
    group_name = models.CharField(max_length=100, unique=True, default = shortuuid.uuid)
    user_online = models.ManyToManyField(User, related_name = 'online_in_groups', blank=True)
    members = models.ManyToManyField(User, related_name="chat_groups", blank =True )
    is_private = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.group_name
    
class ChatMessage(models.Model):
    group = models.ForeignKey(ChatGroup,related_name="chat_messages" ,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author.username} : {self.body}'
    
    class Meta:
        ordering =['-created']
    