from django.contrib.gis.db import models


class Station(models.Model):
	'''
	Models a station
	'''
	class Meta:
        required_db_features = ['gis_enabled']

    location = models.PointField(srid=4326)
    name = models.CharField(max_length=50, null=True)
