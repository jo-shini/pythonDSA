from django.http import JsonResponse, HttpResponse
import json


def hello(request):
    return HttpResponse("Hello from Django")


def create_item(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        return JsonResponse({"ok": True, "item": data}, status=201)
    return JsonResponse({"detail": "Use Post"}, status=405)
