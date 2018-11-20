from django.contrib.gis.db import models
from .route import Route


class Drone(models.Model):
	'''
	Models a drone
	'''
	class Meta:
        required_db_features = ['gis_enabled']

    location = models.PointField(srid=4326)
    launch_time = models.DateTimeField()
    route = models.ForeignKey(Route)

    def __repr__(self):
    	return 'SD_{}'.format(self.id)
