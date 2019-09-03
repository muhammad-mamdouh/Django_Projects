from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import RegistrationSerializer, AccountPropertiesSerializer
from account.models import Account


@api_view(['POST', ])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data       = {}
        if serializer.is_valid():
            account          = serializer.save()
            token            = Token.objects.get(user=account).key
            data['response'] = 'Successfully registered a new user'
            data['email']    = account.email
            data['username'] = account.username
            data['token']    = token
        else:
            data = serializer.errors
        return Response(data=data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def account_properties_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AccountPropertiesSerializer(account)
    return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated, ))
def update_account_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AccountPropertiesSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={'response': 'Account info has been update successfully'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
