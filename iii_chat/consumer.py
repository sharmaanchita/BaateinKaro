from channels.generic.websocket import WebsocketConsumer
from .models import *
from django.shortcuts import get_object_or_404
import json
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync

class ChatroomConsumer(WebsocketConsumer):
    
    def connect(self):
        self.user = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name'] 
        self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)
        
        async_to_sync(self.channel_layer.group_add)(
            self.chatroom_name, self.channel_name
        )
        
        # add and update online users
        if self.user not in self.chatroom.user_online.all():
            self.chatroom.user_online.add(self.user)
            self.handle_online_count()
            self.handle_online_usernames()
        
        self.accept()
        
        
    def disconnect(self, close_code):
        
        async_to_sync(self.channel_layer.group_discard)(
            self.chatroom_name, self.channel_name
        )
        # remove and update online users
        if self.user in self.chatroom.user_online.all():
            self.chatroom.user_online.remove(self.user)
            self.handle_online_count()
            self.handle_online_usernames()
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json.get('body', '') 
        
        message = ChatMessage.objects.create(
            body = body,
            author = self.user, 
            group = self.chatroom 
        )
        event = {
            'type': 'message_handler',
            'message_id': message.id,
        }
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name, event
        )
        
    def message_handler(self, event):        
        message_id = event['message_id']
        message = ChatMessage.objects.get(id=message_id)
        context = {
            'chat': message,
            'user': self.user,
            'chat_group': self.chatroom
        }
        html = render_to_string("iii_chat/partials/chat_load.html", context=context)
        self.send(text_data=html)
        
    def handle_online_count(self):
        online_count = self.chatroom.user_online.count() - 1
        
        event = {
            'type': 'update_count',
            'online_count':online_count,
        }
        
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name, event
        )
        
    def update_count(self, event):
        online_count = event['online_count']
        html = render_to_string("iii_chat/partials/online_count.html", { 'online_count': online_count})
        self.send(text_data=html)
        
    def handle_online_usernames(self):
        online_users = self.chatroom.user_online.all()
        usernames = [user.username for user in online_users]
        
        event = {
            'type': 'update_usernames',
            'usernames': usernames
        }
        
        async_to_sync(self.channel_layer.group_send)(
            self.chatroom_name, event
        )
        
    def update_usernames(self, event):
        usernames = event['usernames']        
        html = render_to_string("iii_chat/partials/online_usernames.html", {'usernames': usernames})
        self.send(text_data=html)
        
        
        
        
        
            

