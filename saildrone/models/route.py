from django.contrib.gis.db import models


class Route(models.Model):
	'''
	Models a drone route
	'''
	class Meta:
        required_db_features = ['gis_enabled']

    route = models.MultiLineStringField(srid=4326)
