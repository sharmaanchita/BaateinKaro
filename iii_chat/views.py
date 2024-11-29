from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

import logging

logger = logging.getLogger(__name__)

# Create your views here.
@login_required
def chat_view(request):    
    chat_gp = get_object_or_404(ChatGroup, group_name="public_chat") 
    chat_messages = chat_gp.chat_messages.all()[:30]
    form = ChatForm()
    
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
    
    return render(request, "iii_chat/chat.html", {"chat_messages":chat_messages, 'form': form})
