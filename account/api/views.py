from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from account.api.serializers import RegistrationSerializer
from account.models import Account

@api_view(['POST'])
def registration_view(request):
    '''Following view is meant to register new users'''

    data = {}
    email = request.data.get('email', '0').lower()
    if validate_email(email) != None:
        data['error_message'] = 'That email is already in use.'
        data['response'] = 'Error'
        return Response(data, status.HTTP_409_CONFLICT)

    username = request.data.get('username', '0')
    if validate_username(username) != None:
        data['error_message'] = 'That username is already in use.'
        data['response'] = 'Error'
        return Response(data, status.HTTP_409_CONFLICT)

    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'successfully registered new user.'
        data['email'] = account.email
        data['username'] = account.username
        data['pk'] = account.pk
        token = Token.objects.get_or_create(user=account).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data, status.HTTP_201_CREATED)

def validate_email(email):
    '''
    This function is to check whether
    username passed already belongs to an
    account or not.
    '''
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account is not None:
        return email

def validate_username(username):
    '''
    This function is to check whether
    username passed already belongs to an
    account or not.
    '''
    account = None
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account is not None:
        return username



class ObtainAuthTokenView(APIView):
    '''
    Following view is to provide requisite information
    to access the app to pre-registered users.
    '''

    def post(self, request):
        context = {}

        email = request.data.get('email')
        password = request.data.get('password')
        account = authenticate(email=email, password=password)

        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['email'] = email.lower()
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'

        return Response(context, status.HTTP_200_OK)
