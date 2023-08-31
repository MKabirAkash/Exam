from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import AdminSerializer,Employeeserializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Employees
from .models import Gadgets,GotGadgetPermission


#VIEW FOR CREATING SUPERUSER
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

#VIEW FOR ADDING NEW EMPLOYEE
@api_view(['POST'])
@csrf_exempt
def addemployee(request):
    try:
        name=request.POST['name']
        position=request.POST['position']
        address=request.POST['address']
        employee=Employees.objects.create(
            name=name,
            position=position,
            address=address
        )
        employee.save()
        return Response({'message': 'Employee addes successfully. (API instruction :PROVIDE A VALID name ,position,address AS REQUEST DATA as as name=set_your_name,position=employee_position and address:set_your_address USING POST METHOD TO MAKE ADMIN USER )'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'message': ' (API instruction :PROVIDE A VALID EMAIL AND PASSWORD AS REQUEST DATA as as email:SET_your_emai and password:set_your_password USING POST METHOD TO MAKE ADMIN USER )'}, status=status.HTTP_400_BAD_REQUEST)


#VIEW FOR ADDING NEW GADGET
@api_view(['POST'])
@csrf_exempt
def addgadget(request):
    try:
        name=request.POST['name']
        condition=request.POST['condition']
        gadget=Gadgets.objects.create(
            name=name,
            present_con=condition
        )
        gadget.save()
        return Response({'message': 'Gadget added successfully. (API instruction :PROVIDE A VALID name ,condittion AS REQUEST DATA as aname=set_your_name,condition=set a value between 1-100 USING POST METHOD TO ADD A NEW EMPLOYEE )'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'message': ' (API instruction :PROVIDE A VALID name,condition AS REQUEST DATA   as name=set_your_name,condition=set a value between 1-100 TO ADD A NEW GADGET )'}, status=status.HTTP_400_BAD_REQUEST)



#VIEW FOR ADDING EMPLOYEE TO PERMIT TO HAVE GADGET(for adding individual employye)

@api_view(['POST'])
@csrf_exempt

def addselected(request,id):
    try:
        emp=Employees.objects.get(_id=id)
        permitted_emp=GotGadgetPermission.objects.create(employee=emp)
        permitted_emp.save()
        return Response({'message': 'permisson granted  successfully fro gadget. (PASS THE EMPLOYEE ID AT END OF THE URI TO SELECT HIM FOR GADGET PERMISSION )'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'message': '(PASS THE EMPLOYEE ID AT END OF THE URI TO SELECT HIM FOR GADGET PERMISSION )'}, status=status.HTTP_400_BAD_REQUEST)




#VIEW FOR ADDING EMPLOYEE TO PERMIT TO HAVE GADGET(for adding individual employye)
@api_view(['POST'])
@csrf_exempt

def addall(request):
    try:
        emp=Employees.objects.all()

        for i in emp:
            permitted_emp=GotGadgetPermission.objects.create(employee=i)
            permitted_emp.save()
        return Response({'message': 'permisson granted  successfully to all employees. ( FOR GADGET PERMISSION )'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'message': '(HIT THE API TO PERMIT ALL FOR GADGET )'}, status=status.HTTP_400_BAD_REQUEST)
