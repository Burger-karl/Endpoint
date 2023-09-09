from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from api.models import Info

# Create your views here.

def get_info(request):
    
    current_day = timezone.now().strftime('%A')

    
    data = {
        'slack_name':'Ifeanyi Charles',
        'current_day': current_day,
        'utc_time': timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'track': 'backend',
        'github_file_url': 'https://github.com/Burger-karl/hngproj/blob/main/projapi/views.py',
        'github_repo_url': 'https://github.com/Burger-karl/hngproj/tree/main',
        'status_code': 200
        }

    return JsonResponse(data)