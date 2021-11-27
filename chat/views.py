from django.shortcuts import redirect, render


def chat(request):
    return redirect('/chat/12345/')


def room(request, room_name):
    return render(request, 'chatroom.html', {'room_name': room_name})
