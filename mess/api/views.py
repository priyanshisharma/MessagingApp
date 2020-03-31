from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from rest_framework.parsers import JSONParser





@api_view(['GET'])
def list(request,username):
    if request.method == 'GET':
        queryset = Message.objects.all()
        for e in Message.objects.all():
            
        serializer = MessageSerializer(queryset,many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create(request):
    data = JSONParser().parse(request) #To be seen
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)