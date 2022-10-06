import json
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import *
from .models import *
import io
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def StudentCreate(request):
    print("*******************")
    data = json.loads(request.body)
    serializer=StudentSerializer(data=data)
    print("_____________")
    print(type(serializer))
    print ('serializer',serializer)
    print("=========================")
    if serializer.is_valid():
        print("=========================")
        serializer.save()
        print("=======================")
        res={'msg':'data saved'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    else:
        print(serializer.errors)
        return HttpResponse("Errors are there")
    # json_data=JSONRenderer().render(serializer.errors)
    # return HttpResponse(json_data,content_type='application/json')

