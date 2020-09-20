"""
    /api/tutorials: GET, POST, DELETE view name tutorial
    /api/tutorials/:id GET PUT DELETE
    /api/tutorials/published GET
"""

from django.shortcuts import render
from rest_framework.decorators import api_view,parser_classes
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from RestMongo.serializers import TutorialSerializer
from RestMongo.models import Tutorial
import json

# Create your views here.


@api_view(['GET','POST','DELETE'])
@parser_classes([JSONParser])
def tutorial_list(request):
    #GET List of Tutorials , Post a new Tutorial , Delete a Tutorial
    if request.method =='GET':
        tutorials = Tutorial.objects.using('mongo_db').all()
        tutorials_s=TutorialSerializer(tutorials,many=True)
        return JsonResponse(tutorials_s.data,safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        # t_data= json.dump(request)
        # print(t_data)
        tutorials_s=TutorialSerializer(data=tutorial_data)
        print(tutorial_data)
        if tutorials_s.is_valid() :
            tutorials_s.save()
            
            return JsonResponse(tutorials_s.data,status=status.HTTP_201_CREATED)
        return JsonResponse(tutorials_s.errors,status = status.HTTP_400_BAD_REQUEST)
            
        
    
@api_view(['GET','PUT','DELETE'])
def tutorial_detail(request, pk):
    
    # Find Tutorial By pk
    try:
        tutorial = Tutorial.objects.using('mongo_db').get(pk=pk)
    except Tutorial.DoesNotExist:
         return JsonResponse({'message':'The Requested Tutorial does not exist'},status=status.HTTP_404_NOT_FOUND)
     
@api_view(['GET'])
def tutorial_list_published(request):
    #Get All Published Tutorials 
    pass