from ipums.models import PUMA
from analysis.datelist import ANNUAL
from nodes.models import NodeTimePoint
from django.conf import settings
import os

def ts_datelist_cum(dates=ANNUAL):
    d = {}
    for date in dates:
        d[date] = PUMA.objects.filter(adoption_date__lte=date).count()
    return d
    

def ts_annual(start=1984, end=2000):
    d = {}
    for year in range(start, end):
        d[year] = PUMA.objects.filter(adoption_date__year=year).count()
    return d

def ts_annual_cum(start=1984, end=2000):
    d = {}
    ts = ts_annual(start, end)
    count = 0
    for y, c in ts.iteritems():
         count += c
         d[y] = count
    return d

def adoption_curve_prop(start=1984, end=2000):
    d = {}
    ts = ts_annual_cum()
    total = PUMA.objects.count()
    for y, c in ts.iteritems():
        d[y] = float(c)/total
    return d

def check_area_codes():
    from area_codes.models import AreaCode

RESULTS_PATH = os.path.join(settings.PROJECT_PATH, 'ipums', 'data')
print RESULTS_PATH

def puma_survival(pumas=PUMA.objects.all(), filename='new_puma_surv.dat'):
    start_date = NodeTimePoint.objects.order_by('date')[0].date
    end_date = NodeTimePoint.objects.order_by('-date')[0].date
    with open(os.path.join(RESULTS_PATH, filename), 'w') as f:
        f.write('strata Week Adoption\n')
        for p in pumas:
            f.write(p.strata_label() + ' ')
            if p.adoption_date:
                f.write('%d %d\n' % ((p.adoption_date - start_date).days/7, 1))
            else:
                f.write('%d %d\n' % ((end_date - start_date).days/7, 0))
