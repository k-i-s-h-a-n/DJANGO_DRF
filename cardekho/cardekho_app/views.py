from django.shortcuts import render
from .models import carList, showroomList
from django.http import JsonResponse


from .api_list.serializers import carSerializer, showroomSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser



# Create your views here.


# def car_list_view(request):
#     cars=carList.objects.all()
#     data={
#         "cars": list(cars.values("id", "name", "description", "active" )  ),
#     }

#     return JsonResponse(data)



# def car_detail_view(request, id):
#     car=carList.objects.get(id=id)
#     data={
#         "id": car.id,
#         "name": car.name,
#         "description": car.description,
#         "active": car.active,
#     }

#     return JsonResponse(data)




@api_view(['GET', 'POST' ])
def car_list_view(request):
    if request.method == 'GET':
        car = carList.objects.all()
        serializer=carSerializer(car, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=carSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method == 'GET':
        try:
            car = carList.objects.get(pk=pk)
        except carList.DoesNotExist:
            return Response({"Error : car not found "},status=404)    
        serializer=carSerializer(car)
        return Response(serializer.data)
    if request.method == 'PUT':
        car = carList.objects.get(pk=pk)
        serializer=carSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=202)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        car = carList.objects.get(pk=pk)
        car.delete()
        return Response(status=204)
    

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    logout(request)
    return redirect('list') 



from rest_framework.views import APIView


class showroom_list_view(APIView):
    # if we want same authentication system and permissions for all functions then we do not wwant to declare it in every view instead of this we can declare one time in settings.py 
    
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAdminUser]


    # Session Authentication
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]


    def get(self, request):
        showroom = showroomList.objects.all()
        serializer=showroomSerializer(showroom, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=showroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class showroom_details(APIView):
    def get(self, request ,pk):
        try:
            showroom = showroomList.objects.get(pk=pk)
        except showroomList.DoesNotExist:
            return Response({"Error : showroom not found "},status=404)
        serializer = showroomSerializer(showroom)
        return Response(serializer.data)
    
    def put(self, request, pk):
        showroom = showroomList.objects.get(pk=pk)
        serializer = showroomSerializer(showroom, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=404)
    

    def delete(self, request, pk):
        showroom = showroomList.objects.get(pk=pk)
        showroom.delete()
        return Response(status=204)
    

    