from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here. api view convert function to api
@api_view(['GET','POST','PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            "status":200,
            "message":"this is a random message",
            'method_called': 'GET method called'
        })
    elif request.method == 'POST':
        return Response({
            "status":201,
            "message":"this is a random message",
            'method_called': 'POST method called'
        })
    elif request.method == 'PATCH':
        return Response({
            "status":200,
            "message":"this is a random message",
            'method_called': 'PATCH method called'
        })
    else:
        return Response({
            "status":400,
            "message":"this is a random message",
            'method_called': 'Bad request'
        })
    
# Serilizer convert query set to json formate, so we can send via HTTP protocol
@api_view(['POST'])
def post_todo(request):
    try:
        get_data = request.data
        serializer = TodoSerializer(data=get_data)
        if serializer.is_valid():
            serializer.save()

            return Response({'status':True,
                'message':'Successfully todo created',
                'data': serializer.data
            })

    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Something went wrong'
        })