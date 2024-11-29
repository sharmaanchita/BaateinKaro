from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import Http404

import logging

logger = logging.getLogger(__name__)

# Create your views here.
@login_required
def chat_view(request, chatroom_name = "public_chat"):    
    chat_gp = get_object_or_404(ChatGroup, group_name=chatroom_name) 
    chat_messages = chat_gp.chat_messages.all()[:30]
    form = ChatForm()
    
    other_user = None
    if chat_gp.is_private:
        if request.user not in chat_gp.members.all():
            raise Http404()
        for member in chat_gp.members.all():
            if member != request.user:
                other_user = member
                break
            
    if request.htmx:
        form = ChatForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_gp
            message.save()
            
            context = {
                'chat': message,
                'user': request.user
            }
            
            return render(request, 'iii_chat/partials/chat_load.html', context)
        
    context={
        "chat_messages":chat_messages, 
        'form': form, 
        "other_user": other_user,
        "chatroom_name": chatroom_name,
    }
    
    return render(request, "iii_chat/chat.html", context)

@login_required
def get_or_create_chatroom(request, username):
    if request.user.username == username:
        return redirect("home")
    
    other_user = User.objects.get(username = username)
    my_chatrooms = request.user.chat_groups.filter(is_private = True)
    
    if my_chatrooms.exists():
        for chatroom in my_chatrooms:
            if other_user in chatroom.members.all():
                chatroom = chatroom
                break
            else:
                chatroom = ChatGroup.objects.create(is_private = True)
                chatroom.members.add(other_user, request.user)
    else:
        chatroom = ChatGroup.objects.create(is_private = True)
        chatroom.members.add(other_user, request.user)
    
    return redirect("chatroom" , chatroom.group_name)
        
                
    
    
