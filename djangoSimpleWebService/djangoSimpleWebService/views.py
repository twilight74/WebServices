from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        response = JsonResponse({"message": "You are in Home Page"})
        del response['Content-Type']
        response['content-type'] = 'application/json'
        del response['content-Length']
        response['content-length'] = 35
        del response['X-Frame-Options']
        response['x-frame-options'] = "X"
        del response['X-Content-Type-Options']
        response['x-content-type-options'] = "X"
        del response['Referrer-Policy']
        response['referrer-policy'] = "X"
        del response['Cross-Origin-Opener-Policy']
        response['cross-origin-opener-policy'] = "X"
        return response
