from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# basic url just to test if the app is working
@api_view()
def testCore(request):
    return Response('ok')