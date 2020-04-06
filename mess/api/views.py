from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from mess.models import Message
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request,username):
    data = dict()
    data["text"] = request.data.get("text") #To be seen
    data["username"] = username
    if request.data.get("author"):
     #   data["is_anonymous"] = request.data.get("is_anonymous")
        data["author"] = request.user.username
    else :
        data["author"] = "Anonymous"
   # if is_anonymous:
    #    author = models.CharField(max_length=200, default = " ")    
    serializer = MessageSerializer(data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list(request,username):
    if request.method == 'GET':
        queryset = Message.objects.filter(username__exact=username)
        serializer = MessageSerializer(queryset,many=True)       
        return Response(serializer.data)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def message_detail(request, pk):
    try:
        messag = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    serializer = MessageSerializer(messag)
    serializer.data['pk'] = messag.pk
    return Response(serializer.data)

#@api_view(['POST'])
#def create(request):
#    data = JSONParser().parse(request) #To be seen
#    serializer = PostSerializer(data=data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data, status=201)
#    return Response(serializer.errors, status=400)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete(request,pk):
    try:
        messa = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return HttpResponse(status=404)
    operation = messa.delete()
    data = dict()
    if operation:
        data["success"] = "delete successful"
    else:
        data["failure"] = "delete failed"
    return Response(data=data)



#@csrf_exempt
#@api_view(['POST'])
#@permission_classes((AllowAny,))
#def login(request):
#    if request.method == 'POST':
#        email = request.data.get("email")
#        password = request.data.get("password")
#        username = request.data.get("username")
#        if username is None or password is None:
#            return Response({'error': 'Please provide both email and password'},status=HTTP_400_BAD_REQUEST)
#        user = authenticate(email=email, password=password)
#        if not user:
#            return Response({'error': 'Invalid Credentials'},
#                            status=HTTP_404_NOT_FOUND)
#        queryset = Message.objects.filter(username__exact=username)
        #queryset = Message.objects.all()       
#        serializer = MessageSerializer(queryset,many=True)
#        return Response(serializer.data)
'''
@api_view(['GET'])
def list(request,username):
    if request.method == 'GET':
'''