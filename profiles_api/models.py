from django.db import models

# Create your models here.
class TvLink(models.Model):
    """Database models for Live TV App"""
    tv1name = models.CharField(max_length=300,null=True, blank=True)
    tv1link = models.CharField(max_length=300,null=True, blank=True)
    tv1ylink = models.CharField(max_length=300,null=True, blank=True)

    tv2name = models.CharField(max_length=300,null=True, blank=True)
    tv2link = models.CharField(max_length=300,null=True, blank=True)
    tv2ylink = models.CharField(max_length=300,null=True, blank=True)

    tv3name = models.CharField(max_length=300,null=True, blank=True)
    tv3link = models.CharField(max_length=300,null=True, blank=True)
    tv3ylink = models.CharField(max_length=300,null=True, blank=True)

    tv4name = models.CharField(max_length=300,null=True, blank=True)
    tv4link = models.CharField(max_length=300,null=True, blank=True)
    tv4ylink = models.CharField(max_length=300,null=True, blank=True)

    tv5name = models.CharField(max_length=300,null=True, blank=True)
    tv5link = models.CharField(max_length=300,null=True, blank=True)
    tv5ylink = models.CharField(max_length=300,null=True, blank=True)

    def __str__(self):
        """To String Method"""
        tv_list = "ALL TV LINKS"
        return tv_list


class AdsService(models.Model):
    """Database model for Ads Service"""
    selectedAddService = models.CharField(max_length=20, default="google")
    status = models.CharField(max_length=10, default="yes")
    cnt = models.IntegerField()

    def __str__(self):
        """To String Method"""
        return "ADS SERVICE"