from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "chat/index.html")


def select_role(request):
    username = request.GET.get("username", "Anonymous")
    room_name = "private_room"
    return render(
        request,
        "chat/agent.html",
        {"room_name": room_name, "username": username},
    )
