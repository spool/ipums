import os
from django.contrib.gis.utils import LayerMapping
from models import PUMA, puma_mapping

usa_contiguous = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/us1990_5.shp'))

def run(verbose=True):
    lm = LayerMapping(PUMA, usa_contiguous, puma_mapping)
    lm.save(strict=True, verbose=verbose)
