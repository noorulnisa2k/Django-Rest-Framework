from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializer import TodoSerializer, TimingTodoSerializer
from .models import Todo, TodoTiming
from rest_framework.permissions import IsAuthenticated

#  >>>>>>>>>>> Classs based view
class TodoView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
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
                'data':serializer.errors
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

    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TodoTiming.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'Status':True,
            'message':'Timing Todo fetched',
            'data':serializer.data
        })

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'Status':True,
                    'message':'Successfully saved',
                    'data': serializer.data
                })
            return Response({
                'Status':False,
                'message':'Invalid Data',
                'data':serializer.errors
            })
        except Exception as e:
            return Response({
                'Status':False,
                'message':'Something went wrong',
                'error': e
            })