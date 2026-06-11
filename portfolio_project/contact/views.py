from django.http import JsonResponse
from .models import ContactMessage
import json

def contact_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ContactMessage.objects.create(
            name=data.get('name'),
            email=data.get('email'),
            message=data.get('message')
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
