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

#class UserCreateAPIView(CreateAPIView):
#    serializer_class = UserCreateSerializer
#    queryset = User.objects.all()
#    permission_classes = [AllowAny]


@api_view(['POST'])
def create(request,username):
    data = dict()
    data["text"] = request.data.get("text") #To be seen
    data["username"] = username
    if request.data.get("author"):
        data["author"] = request.data.get("author")
    serializer = MessageSerializer(data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


#@csrf_exempt
#@api_view(['POST'])
#@permission_classes((AllowAny,))
#def login(request):
#    if request.method == 'POST':
#        username = request.data.get("username")
#        password = request.data.get("password")
#        if username is None or password is None:
#            return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
#        user = authenticate(username=username, password=password)
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