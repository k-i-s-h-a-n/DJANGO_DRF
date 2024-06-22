from django.shortcuts import render
from.models import carList
from django.http import JsonResponse


from .api_list.serializers import carSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



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




@api_view()
def car_list_view(request):
    car = carList.objects.all()
    serializer=carSerializer(car, many=True)
    return Response(serializer.data)


@api_view()
def car_detail_view(request,pk):
    car = carList.objects.get(pk=pk)
    serializer=carSerializer(car)
    return Response(serializer.data)