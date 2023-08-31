from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import AdminSerializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def createadmin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_superuser(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )
        return Response({'message': 'Superuser created successfully. (API instruction :PROVIDE A VALID EMAIL AND PASSWORD AS REQUEST DATA as as email:SET_your_emai and password:set_your_password USING POST METHOD TO MAKE ADMIN USER )'}, status=status.HTTP_201_CREATED)
    return Response({'message':'PROVIDE A VALID EMAIL AND PASSWORD AS REQUEST DATA USING POST METHOD TO MAKE ADMIN USER '}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def addemployee(request):
    return Response("akash")