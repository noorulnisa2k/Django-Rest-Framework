from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import TodoSerializer
from .models import Todo

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
        data = request.data
        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':True,
                'message':'Successfully todo created',
                'data': serializer.data
            })
        
        return Response({
            'status':False,
            'message':'Invalid Data',
            'data': serializer.data
            
        })

    except Exception as e:
        return Response({
            'status':False,
            'message':'Something went wrong',
            'error': e
            
        })
    
@api_view(['GET'])
def get_todo(request):
    try:
        get_data = Todo.objects.all()
        serializer = TodoSerializer(get_data, many = True)
        return Response({'Status':True,
                         'data':serializer.data
        })
    except Exception as e:
        print(e)


# PUT: need to add complete instance of the object while updating a class
        

# PATCH: is partial update, we don't neet to give complete instance but only the field we want to update
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
            'status':False,
            'message':'Uid required'
        })
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status':True,
                'message':'Data Successfully updated',
                'data':serializer.data
            })
    except Exception as e:
        print(e)
        return Response({
            'Status':False,
            'message':'Invalid Uid'
        })
    pass

#  >>>>>>>>>>> Classs based view
class TodoView(APIView):

    # Get request
    def get(self, request):
        try:
            data = Todo.objects.all()
            serializer =  TodoSerializer(data, many=True)
            return Response({
                'Status':True,
                'message':'This is a get request',
                'data':serializer.data
            })
        except Exception as e:
            return Response({
                'status': False,
                'error': e
            })
    
    # Post Request
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':True,
                    'message': 'Data succesfully added',
                    'data':serializer.data
                })
            
            return Response({
                'Status':False,
                'message':'Invalid data',
                'data':serializer.data
            })
        except Exception as e:
            return Response({
                'status':False,
                'message':'something went wrong',
                'error':e
            })


#   >>>>>>>>>>>>>>>>> Viewsets
        
class TodoViewSets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer