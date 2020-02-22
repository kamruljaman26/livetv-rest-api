from django.db import models

# Genarel Live TV
class TvLink(models.Model):
    """Database models for Live TV App"""
    tv1name = models.CharField(max_length=300, blank=True)
    tv1link = models.CharField(max_length=300, blank=True)
    tv1ylink = models.CharField(max_length=300, blank=True)

    tv2name = models.CharField(max_length=300, blank=True)
    tv2link = models.CharField(max_length=300, blank=True)
    tv2ylink = models.CharField(max_length=300, blank=True)

    tv3name = models.CharField(max_length=300, blank=True)
    tv3link = models.CharField(max_length=300, blank=True)
    tv3ylink = models.CharField(max_length=300, blank=True)

    tv4name = models.CharField(max_length=300, blank=True)
    tv4link = models.CharField(max_length=300, blank=True)
    tv4ylink = models.CharField(max_length=300, blank=True)

    tv5name = models.CharField(max_length=300, blank=True)
    tv5link = models.CharField(max_length=300, blank=True)
    tv5ylink = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """To String Method"""
        tv_list = "ALL TV LINKS"
        return tv_list

# PSL Live TV
class PslTvLink(models.Model):
    """Database models for PSL Live TV App"""
    tv1name = models.CharField(max_length=300, blank=True)
    tv1link = models.CharField(max_length=300, blank=True)
    tv1ylink = models.CharField(max_length=300, blank=True)

    tv2name = models.CharField(max_length=300, blank=True)
    tv2link = models.CharField(max_length=300, blank=True)
    tv2ylink = models.CharField(max_length=300, blank=True)

    tv3name = models.CharField(max_length=300, blank=True)
    tv3link = models.CharField(max_length=300, blank=True)
    tv3ylink = models.CharField(max_length=300, blank=True)

    tv4name = models.CharField(max_length=300, blank=True)
    tv4link = models.CharField(max_length=300, blank=True)
    tv4ylink = models.CharField(max_length=300, blank=True)

    tv5name = models.CharField(max_length=300, blank=True)
    tv5link = models.CharField(max_length=300, blank=True)
    tv5ylink = models.CharField(max_length=300, blank=True)

    def __str__(self):
        """To String Method"""
        tv_list = "PSL TV LINKS"
        return tv_list


# Ads Service Data
class AdsService(models.Model):
    """Database model for Ads Service"""
    selectedAddService = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, blank=True)
    cnt = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """To String Method"""
        return "ADS SERVICE"



"""PSL Match Schedule"""
class MatchSchedule(models.Model):
    """Match Schedule"""
    team1name = models.CharField(max_length=100,blank=False, null=False)
    team2name = models.CharField(max_length=100,blank=False, null=False)
    team1logo = models.FileField(blank=False, null=False)
    team2logo = models.FileField(blank=False, null=False)
    matchdate = models.DateField(blank=False,null=False)
    matchtime = models.TimeField(blank=False,null=False)
    matchvenue = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        """To String Method"""
        return self.team1name + " vs " + self.team2name

"""PSL Match Schedule"""
class IplMatchSchedule(models.Model):
    """Match Schedule"""
    team1name = models.CharField(max_length=100,blank=False, null=False)
    team2name = models.CharField(max_length=100,blank=False, null=False)
    team1logo = models.FileField(blank=False, null=False)
    team2logo = models.FileField(blank=False, null=False)
    matchdate = models.DateField(blank=False,null=False)
    matchtime = models.TimeField(blank=False,null=False)
    matchvenue = models.CharField(max_length=255,blank=False,null=False)

    def __str__(self):
        """To String Method"""
        return self.team1name + " vs " + self.team2name

"""News Database Model"""
class MatchNews(models.Model):
    """News Models"""
    title = models.CharField(max_length=100,blank=False, null=False)
    url = models.URLField(max_length=250,blank=False,null=False)
    sourcename = models.CharField(max_length=100,blank=False, null=False)
    image = models.FileField(blank=False, null=False)

    def __str__(self):
        """To Sting Method"""
        return  self.title



