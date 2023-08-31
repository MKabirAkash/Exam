from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import AdminSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def createadmin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_superuser(
            username=serializer.validated_data['email'],
            password=make_password(serializer.validated_data['password'])
        )
        return Response({'message': 'Superuser created successfully'}, status=status.HTTP_201_CREATED)
    return Response({'message':'PROVIDE A VALID EMAIL AND PASSWORD AS REQUEST DATA USING POST METHOD TO MAKE ADMIN USER '}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method=='POST':
        uname=request.POST['username']
        password=request.POST['password']

        log_user=auth.authenticate(username=uname,password=password)
        if log_user is not None:
            auth.login(request,log_user)
            return Response({'message': 'Superuser created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'GIVE USERNAME AND ASSOCIATED PASSWORD TO LOGIN USING POST METHOD'}, status=status.HTTP_400_BAD_REQUEST)