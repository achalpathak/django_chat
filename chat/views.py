from django.shortcuts import render
from .models import Agents, Customers, Messages

# Create your views here.


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    username = request.GET.get("username", "Anonymous")
    role = request.GET.get("role", None)
    errors = []
    if role not in ["agent", "customer"]:
        errors.append("Invalid role input.")
    elif role == "agent":
        agent = Agents.objects.filter(username=username).first()
        if not agent:
            errors.append("Username doesnt exists.")
    elif role == "customer":
        customer = Customers.objects.filter(username=username).first()
        if not customer:
            errors.append("Username doesnt exists.")
    if errors:
        return render(
            request,
            "chat/index.html",
            {"errors": errors},
        )
    messages = Messages.objects.filter(room=room_name)

    return render(
        request,
        "chat/room.html",
        {
            "room_name": room_name,
            "role": room_name,
            "username": username,
            "messages": messages,
        },
    )
