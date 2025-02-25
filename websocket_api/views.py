#from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
import api_sy


# Create your views here.
def index(request):
    return JsonResponse({"message": "WebSocket API is working!"})
    
def chatTest(request, room_name):
    return render(request, "websocket_api/chat_test.html", {"room_name" : room_name})

def apiTest(reqeust):
    gp = api_sy.GooglePlace()
    place_id = gp.get_restaurant_details("시래마루 이천점")
    return JsonResponse({"place_id": place_id})
