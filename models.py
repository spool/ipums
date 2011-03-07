# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class PUMA(models.Model):
    objectid = models.IntegerField()
    gismatch = models.IntegerField()
    statefip = models.CharField(max_length=2)
    puma = models.CharField(max_length=5)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for PUMA model
puma_mapping = {
    'objectid' : 'OBJECTID',
    'gismatch' : 'GISMATCH',
    'statefip' : 'STATEFIP',
    'puma' : 'PUMA',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'geom' : 'POLYGON',
}
