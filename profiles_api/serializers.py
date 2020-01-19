from rest_framework import serializers
from profiles_api import models

class TvLinkSerializer(serializers.ModelSerializer):
    """Serializer for TV Link"""

    class Meta:
        model = models.TvLink
        fields = (
            'id',
            'tv1name','tv1link','tv1ylink',
            'tv2name', 'tv2link', 'tv2ylink',
            'tv3name', 'tv3link', 'tv3ylink',
            'tv4name', 'tv4link', 'tv4ylink',
            'tv5name', 'tv5link', 'tv5ylink'
        )


class AdsServiceSerializer(serializers.ModelSerializer):
    """Serializer for Ads Service"""

    class Meta:
        model = models.AdsService
        fields = (
            'selectedAddService',
            'status',
            'cnt'
        )