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

class PslTvLinkSerializer(serializers.ModelSerializer):
    """PSL Serializer for TV Link"""
    class Meta:
        model = models.PslTvLink
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


class MatchScheduleSerializer(serializers.ModelSerializer):
    """Data Serializer for Match Schedule"""

    class Meta:
        model = models.MatchSchedule
        fields = (
            'id',"match_status",
            "team1name",
            "team2name",
            "team1logo",
            "team2logo",
            "matchdate",
            "matchtime",
            "matchvenue"
        )

class IplMatchScheduleSerializer(serializers.ModelSerializer):
    """Data Serializer for Match Schedule"""

    class Meta:
        model = models.IplMatchSchedule
        fields = (
            'id',"match_status",
            "team1name",
            "team2name",
            "team1logo",
            "team2logo",
            "matchdate",
            "matchtime",
            "matchvenue"
        )

class NewsSerializer(serializers.ModelSerializer):
    """News Serializer"""
    class Meta:
        model = models.MatchNews
        fields = (
            'id',
            'title',
            'url',
            'sourcename',
            'image',
        )

class VersionSerializer(serializers.ModelSerializer):
    """News Serializer"""
    class Meta:
        model = models.VERSION
        fields = (
            'id',
            'version',
        )



class PlayerSeriaziler(serializers.ModelSerializer):
    """Player Seriaziler"""
    class Meta:
        model = models.Player
        fields = ['id','player_name','player_image']


class TeamSerializer(serializers.ModelSerializer):
    """Team Serializer"""
    player = PlayerSeriaziler(many=True, read_only=True)

    class Meta:
        model = models.Team
        fields = ['id', 'team_name', 'team_image','player']