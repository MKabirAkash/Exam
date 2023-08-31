from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializer import AdminSerializer,Employeeserializer
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import Employees
from .models import Gadgets,GotGadgetPermission,Gadgettrackinfo
from datetime import datetime


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
        return Response({'message': 'Error occured.pass the para meter data Correctly . (API instruction :PROVIDE A VALID name ,position,address AS REQUEST DATA as as name=set_your_name,position=employee_position and address:set_your_address USING POST METHOD TO MAKE ADMIN USER  )'}, status=status.HTTP_400_BAD_REQUEST)


#VIEW FOR ADDING NEW GADGET
@api_view(['POST'])
@csrf_exempt
def addgadget(request):
    try:
        name=request.POST['name']
        gadget=Gadgets.objects.create(
            name=name
        )
        gadget.save()
        return Response({'message': 'Gadget added successfully. (API instruction :PROVIDE A VALID name ,AS REQUEST DATA as aname=set_your_name USING POST METHOD TO ADD A NEW EMPLOYEE )'}, status=status.HTTP_201_CREATED)
    except:
        return Response({'message': 'Error occured.pass the para meter data Correctly . (API instruction :PROVIDE A VALID name, REQUEST DATA   as name=set_your_name TO ADD A NEW GADGET )'}, status=status.HTTP_400_BAD_REQUEST)



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
        return Response({'message': 'Error occured.pass the para meter data Correctly .(PASS THE EMPLOYEE ID AT END OF THE URI TO SELECT HIM FOR GADGET PERMISSION )'}, status=status.HTTP_400_BAD_REQUEST)




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
        return Response({'message': 'Error occured.pass the para meter data Correctly .(HIT THE API TO PERMIT ALL FOR GADGET )'}, status=status.HTTP_400_BAD_REQUEST)



#VIEW FOR ALLOTING A GADGET TO A EMPLOYEE
@api_view(['POST'])
@csrf_exempt
def allotgadget(request):
    try:
        emp_id=int(request.POST['employee_id'])
        gad_id=int(request.POST['gadget_id'])
        condition=request.POST['condition']
        print(condition)
        emp=Employees.objects.get(_id=emp_id)
        gadget=Gadgets.objects.get(_id=gad_id)
        trackinfo=Gadgettrackinfo.objects.create(
            employee=emp,
            gadget=gadget,
            last_chek_con=condition
        )
        time=trackinfo.created_at
        gadget.is_checked_out=True
        trackinfo.checkout_at=time
        print(trackinfo.checkout_at)
        trackinfo.save()
        gadget.save()
        return Response({'message':'Gadget alloted to Selected Employee.(API INFO : add as employee_id=desired_employee_id ,condition=gadget_condition_now and gadget_id=desired_gadget_id  TO ALLOT GADGET TO AN EMPLOYEE.MAKE SURE THAT  THE PRODUCT AND EMPLOYEE EXISTS AND GADGET IS NOT ALREADY ALLOTED TO SOMEONE)'})
    except:
        return Response({'message':'Error occured.pass the para meter data Correctly .(API INFO : add as employee_id=desired_employee_id,condition=gadget_condition_now  and gadget_id=desired_gadget_id  TO ALLOT GADGET TO AN EMPLOYEE,MAKE SURE THAT  THE PRODUCT AND EMPLOYEE EXISTS AND GADGET IS NOT ALREADY ALLOTED TO SOMEONE)'},status=status.HTTP_400_BAD_REQUEST)




#VIEW FOR RETURNING A GADGET FROM A EMPLOYEE
@api_view(['POST'])
@csrf_exempt
def gadgetrecord(request,id):
    try:
        track_record=Gadgettrackinfo.objects.get(_id=id)
        gadget=Gadgets.objects.get(name=track_record.gadget)
        gadget.is_checked_out=False
        gadget.save()
        track_record.return_con=request.POST['condition']
        track_record.is_returned=True
        track_record.returned_at=datetime.now
        track_record.save()
        return Response({'message':'Gadget returend from Employee.(API INFO : add as condition=gadget_condition_now TO verify return condition)'})
    except:
        return Response({'message':'Error occured. pass the para meter data Correctly .(API INFO : add as condition=gadget_condition_now TO verify return condition)'},status=status.HTTP_400_BAD_REQUEST)
