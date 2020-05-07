from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_hotels


class Index(APIView):

    @staticmethod
    def get(request):
        return Response({
            "message": "Hi Tairu"
        })


class GetPropertyView(APIView):

    @staticmethod
    def get(request):
        lat_and_long = request.GET.get('at')
        if not lat_and_long:
            return Response({"error": "lat is necessary"})
        if not len(lat_and_long.split(',')) == 2:
            return Response({"error": "invalid data for longitude and latitude"})

        lat_and_long = lat_and_long.split(',')
        response = get_hotels(lat_and_long[0], lat_and_long[1])
        return Response(response)
