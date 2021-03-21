from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from core.handlers.dispatcher import process_telegram_event
from app_my_places.settings import TELEGRAM_TOKEN

import json

# Create your views here.
def index(request):
    return JsonResponse({"error": "forbidden"})

class TelegramBotWebhookView(View):

    def post(self, request, *args, **kwargs):
        process_telegram_event(json.loads(request.body))
        return JsonResponse({"post": "work!"})

    def get(self, request, *args, **kwargs):
        return JsonResponse({"ok": "Get response work!"})


