from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def join(request):
    return render(request, 'chat/join.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })