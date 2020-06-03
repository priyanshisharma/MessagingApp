from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from mess.models import Message
from .serializers import MessageSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request, username):
    '''
    This Creates a message to a particular
    username from the authenticated user.
    '''

    data = dict()
    data["text"] = request.data.get("text")
    data["username"] = username

    '''
    If the user wishes to be the author, it needs to
    specify the author key of their message. Else
    it will be filled with anonymous.
    '''
    if request.data.get("author"):
        '''The author shall be the username irrespective of the author entered.'''
        data["author"] = request.user.username
    else:
        data["author"] = "Anonymous"

    serializer = MessageSerializer(data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list(request, username):
    '''This lists the all the messages directed to a particular user.'''
    queryset = Message.objects.filter(username__exact=username)
    serializer = MessageSerializer(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def message_detail(request, pk):
    '''This allows the user to view a particular message'''
    try:
        messag = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response({"details":"Message Does Not Exist"}, status.HTTP_404_NOT_FOUND)

    serializer = MessageSerializer(messag)
    serializer.data['pk'] = messag.pk
    return Response(serializer.data, status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete(request, pk):
    '''This allows a user to delete its message'''
    try:
        messa = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response({"detail":"Message does not exist"}, status.HTTP_404_NOT_FOUND)
    operation = messa.delete()

    res = dict()
    if operation:
        res["success"] = "delete successful"
    else:
        res["failure"] = "delete failed"

    return Response(res, status.HTTP_200_OK)
