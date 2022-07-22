from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status

from super_types.models import SuperType
from .serializers import SuperSerializer
from .models import Super
from super_types.serializers import SuperTypeSerializer

@api_view(['GET', 'POST'])
def supers_list(request):
    supers = Super.objects.all()
    supe_type = request.query_params.get('type')
    type_supe = SuperType.objects.all()
    if request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET' and supe_type:
        supers = supers.filter(super_type__type=supe_type)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    else:
        heroes = Super.objects.filter(super_type_id=1)
        hero_serializer = SuperSerializer(heroes, many=True)
        villains = Super.objects.filter(super_type_id=2)
        villian_serializer = SuperSerializer(villains, many=True)
        custom_response = {
            'heroes': hero_serializer.data,
            'villains': villian_serializer.data
        }
        return Response(custom_response, status=status.HTTP_200_OK)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET'])
# def get_custom_dict(request):
#    supes = Super.ojbects.all()
#    supetype = SuperType.objects.all()
   
#    supes_serializer = SuperSerializer(supes, many=True)
#    supetype_serializer = SuperTypeSerializer(supetype, many=True)
   
#    custom_dict_response ={
#        'heroes': supes_serializer.data,
#        'villains': supetype_serializer.data
#    }

#    return Response(custom_dict_response)