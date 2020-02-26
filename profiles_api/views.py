from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from fcm_django.models import FCMDevice


class LiveTvViewSet(viewsets.ModelViewSet):
    """Handle createing, reading and updating LiveTv API Data"""
    serializer_class = serializers.TvLinkSerializer
    queryset = models.TvLink.objects.all()
    #http_method_names allows only defined http method
    http_method_names = ['get']

class PslLiveTvViewSet(viewsets.ModelViewSet):
    """Handle createing, reading and updating PSL LiveTv API Data"""
    serializer_class = serializers.PslTvLinkSerializer
    queryset = models.PslTvLink.objects.all()
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


class MatchSchedule(viewsets.ModelViewSet):
    """Handle createing, reading and updating Match Schedule"""
    serializer_class = serializers.MatchScheduleSerializer
    queryset = models.MatchSchedule.objects.all()

    #http_method_names allows only defined http method
    http_method_names = ['get','post','put']

    def post(self, request, *args, **kwargs):

      file_serializer = serializers.MatchScheduleSerializer(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IplMatchSchedule(viewsets.ModelViewSet):
    """Handle createing, reading and updating Match Schedule"""
    serializer_class = serializers.IplMatchScheduleSerializer
    queryset = models.IplMatchSchedule.objects.all()

    #http_method_names allows only defined http method
    http_method_names = ['get','post','put']

    def post(self, request, *args, **kwargs):

      file_serializer = serializers.MatchScheduleSerializer(data=request.data)
      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchNews(viewsets.ModelViewSet):
    """Handle createing, reading and updating Match Schedule"""
    serializer_class = serializers.NewsSerializer
    queryset = models.MatchNews.objects.all()

    #http_method_names allows only defined http method
    http_method_names = ['get','post','put']

    def post(self, request, *args, **kwargs):
      file_serializer = serializers.NewsSerializer(data=request.data)
      if file_serializer.is_valid():

          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VERSIONViewSet(viewsets.ModelViewSet):
    """Handle createing, reading and updating LiveTv API Data"""
    serializer_class = serializers.VersionSerializer
    queryset = models.VERSION.objects.all()
    #http_method_names allows only defined http method
    http_method_names = ['get']