
# Create your views here.
from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class LiveTvViewSet(viewsets.ModelViewSet):
    """Handle createing, reading and updating LiveTv API Data"""
    serializer_class = serializers.TvLinkSerializer
    queryset = models.TvLink.objects.all()
    #http_method_names allows only defined http method
    http_method_names = ['get']

class AdserviceViewSet(viewsets.ModelViewSet):
    """Handle createing, reading and updating Ads Service"""
    serializer_class = serializers.AdsServiceSerializer
    queryset = models.AdsService.objects.all()
    #http_method_names allows only defined http method
    http_method_names = ['get']

    def list(self, request):
        serializer = serializers.AdsServiceSerializer(self.queryset, many=True)
        return Response(serializer.data)
