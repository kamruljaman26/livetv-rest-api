from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.TvLink) # General Tv Link
admin.site.register(models.PslTvLink) # PSL TV Links
admin.site.register(models.AdsService) # Ads Service Data
admin.site.register(models.MatchSchedule) # PSL SCHEDULE
admin.site.register(models.IplMatchSchedule) #IPL SCHEDULE
admin.site.register(models.MatchNews) # ALL SPORTS NEWS
admin.site.register(models.VERSION) # ALL VERSION NEWS
admin.site.register(models.Team) # ALL VERSION NEWS
admin.site.register(models.Player) # ALL VERSION NEWS
