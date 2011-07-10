# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models
from datetime import date
import fips
from fips.fields import USStateFipsField, USStateFipsCode

class PUMA(models.Model):
    objectid = models.IntegerField()
    gismatch = models.IntegerField()
    statefip = models.CharField(max_length=2)
    state = USStateFipsField(null=True)
    puma = models.CharField(max_length=5)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    adoption_date = models.DateField(blank=True, null=True)
    deadoption_date = models.DateField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return '%s (%s)' % (self.puma, fips.US_STATE_FIPS[self.statefip])

    def time_series(self, start=1984, end=2004):
        d = {}
        for year in range(start, end):
            if self.node_time_points:
                d[year] = self.node_time_points.filter(date__year=year).count()
            else:
                d[year] = 0
        return d

    def strata_label(self):
        return self.statefip + self.puma

    def previous_adoption_ts(self, start=1984, end=2004):
        d = {}
        for year in range(start, end):
            if self.adoption_date < date(year, 1, 1):
                d[year] = 1
            else:
                d[year] = 0
        return d

    def set_adoption_date(self):
        if self.node_time_points.all():
            self.adoption_date = self.node_time_points.order_by('date')[0].date
            self.save()

    def set_deadoption_date(self):
        if self.node_time_points.all():
            self.deadoption_date = self.node_time_points.order_by('-date')[0].date
            self.save()

    def set_state(self):
        self.state = USStateFipsCode(self.statefip)
        self.save()


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
