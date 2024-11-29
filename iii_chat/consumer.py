from channels.generic.websocket import WebsocketConsumer
from .models import *
from django.shortcuts import get_object_or_404
import json
from django.template.loader import render_to_string

class ChatroomConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['chatroom_name']
        try:
            self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)
            self.accept()
            print(f"Connected to chatroom: {self.chatroom_name}")
        except Exception as e:
            print(f"Connection failed: {e}")
            self.close()
        
        
    def receive(self, text_data):
        
        try:
            text_data_json = json.loads(text_data)
            body = text_data_json.get('body')
     
            message = ChatMessage.objects.create(
                body=body,
                author=self.user,
                group=self.chatroom
            )
            
            context = {'chat': message, 'user': self.user}
            html = render_to_string('iii_chat/partials/chat_load.html', context=context)
            
            # Send the HTML back to the client
            self.send(text_data=html)
            
        except Exception as e:
            print(f"Error in receive: {e}")
        