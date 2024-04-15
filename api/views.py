from rest_framework.response import Response
from rest_framework.decorators import api_view

from fitness.models import BodyComposition
from .serializers import BodyCompositionSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All Body Comp Data': '/bodycomp/all',
        'Single Body Comp Data': '/bodycomp/<str:pk>',
        'Add Body Comp Data': '/bodycomp-add',
        'Update Body Comp Data': '/bodycomp-update/<str:pk>',
        'Delete Body Comp Data': '/bodycomp-delete/<str:pk>',
    }

    return Response(api_urls)

@api_view(['GET'])
def getAllBodyCompData(request):
    test = {
        '1': 'test 1',
        '2': 'test 2',
        '3': 'test 3',
    }

    body_comp = BodyComposition.objects.all()
    serializer = BodyCompositionSerializer(body_comp, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBodyCompData(request, pk):
    body_comp = BodyComposition.objects.get(id=pk)
    serializer = BodyCompositionSerializer(body_comp, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addBodyCompData(request):
    serializer = BodyCompositionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['POST'])
def updateBodyCompData(request, pk):
    body_comp = BodyComposition.objects.get(id=pk)
    serializer = BodyCompositionSerializer(instance=body_comp, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteBodyCompData(request, pk):
    body_comp = BodyComposition.objects.get(id=pk)
    body_comp.delete()

    return Response("Body Composition Deleted")