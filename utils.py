from area_codes.models import AreaCode
from ipums.models import PUMA
from django.conf import settings
import os

RESULTS_PATH = os.path.join(settings.PROJECT_PATH, 'ipums', 'data')

def set_pumas(area_codes = AreaCode.us.all()):
    errors = []
    for code in area_codes:
        try:
            code.set_puma()
        except:
            print code
            errors.append(code)
    return errors

def geojson_list(list, point_name="geom.centroid"):
    template = '{ "type": "Point", "coordinates": [ %f, %f ] }'

def puma_survival(pumas=PUMA.objects.all(), filename='puma_surv.dat'):
    start_date = PUMA.objects.order_by('adoption_date')[0].adoption_date
    with open(os.path.join(RESULTS_PATH, filename), 'w') as f:
        f.write('strata week adoption\n')
        for puma in pumas:
            f.write(puma.strata_label() + ' ')
            if puma.adoption_date:
                f.write('%d %d\n' % ((puma.adoption_date - start_date).days/7, 1))
            else:
                f.write('NA 0\n')
