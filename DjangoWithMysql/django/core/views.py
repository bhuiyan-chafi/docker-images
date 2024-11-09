from django.http import JsonResponse as response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import User

def testCore(request):
    return response({"message":"Yes your core app is working!"},status=200)
#we are not using the DjangoREST here so by default the application will assume that we are sending it from a html and doing that requires a csrf token. So we disabled it because we are using Postman.
@csrf_exempt
def createUser(request):
    if request.method == "POST":
        #getting data from the request object
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))
        status = True if request.POST.get('status') == 'active' else False
        if not username or not password or not status:
            return response({"message":"all the required fields data are not present"},status=400)
        user = User(username=username, password=password, status=status)
        user.save()
        return response({"data":"user created successfully"},status=201)
    return response({"message":"Only POST method is allowed!"},status=405)

