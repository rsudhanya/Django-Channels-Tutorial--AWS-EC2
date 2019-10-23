from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.


def index(request, room_name = ""):
    if(room_name == ""):
        return render(request, 'chat/index.html', {})
    else:
        print(type(room_name))
        print(room_name)
        return render(request, 'chat/room.html', {
            'room_name_json': mark_safe(json.dumps(room_name))
        })

# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })
