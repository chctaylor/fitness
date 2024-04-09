from rest_framework.response import Response
from rest_framework.decorators import api_view

from fitness.models import BodyComposition
from .serializers import BodyCompositionSerializer


@api_view(['GET'])
def getData(request):
    test = {
        '1': 'test 1',
        '2': 'test 2',
        '3': 'test 3',
    }

    body_comp = BodyComposition.objects.all()
    serializer = BodyCompositionSerializer(body_comp, many=True)
    return Response(serializer.data)