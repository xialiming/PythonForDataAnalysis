# coding=utf

import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\xlm\\Documents\\GitHub\\PythonForDataAnalysis', 'C:/Users/xlm/Documents/GitHub/PythonForDataAnalysis'])
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()
import json
records = [json.loads(line) for line in open(path)]
records[0]
records[0]['tz']
time_zones = [rec['tz'] for rec in records]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]
len(time_zones)
from pandas import DataFrame, Series
import pandas as pd; import numpy as np
frame = DataFrame(records)
frame
tz_counts = frame['tz'].value_counts()
tz_counts[:10]
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10]
tz_counts[:10].plot(kind='barh', rot=0)
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]