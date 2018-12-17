
import pandas as pd

import numpy as np
from numpy.core.multiarray import ndarray

df = pd.read_excel("building_comp.xlsx")

quantity_per_component = df['QPC']

quantity_50th = df['50thQ']

percentage_damaged_low = df['%L']

percentage_damaged_medium = df['%M']

percentage_damaged_high = df['%H']

worker_days_low = df['WL']

worker_days_medium = df['WM']

worker_days_high = df['WH']

total_worker_day_low = df['total_worker_day_low'] = percentage_damaged_low * worker_days_low

total_worker_day_medium = df['total_worker_day_medium'] = percentage_damaged_medium * worker_days_medium

total_worker_day_high = df['total_worker_day_high'] = percentage_damaged_high * worker_days_high



#variabile livello di danno basso (0.2: test_value)
damage_level_low = df['damage_level_low'] = 0.2 * np.ones((16))

#variabile livello di danno medio (0.5: test_value)
damage_level_medium = df['damage_level_medium'] = 0.5 * np.ones((16))

#variabile livello di danno alto (0.9: test_value)

damage_level_high = df['damage_level_high'] = 0.9 * np.ones((16))

defuzzification_low = df['defuzzification_L'] = total_worker_day_low * damage_level_low

defuzzification_medium = df['defuzzification_M'] = total_worker_day_medium * damage_level_medium

defuzzification_high = df['defuzzification_H'] = total_worker_day_high * damage_level_high

#variabile gross area (1400: test value)
gross_area = df['gross_area'] = 1400

#variabile damage (0.5 value_test)
damage = 0.7

if damage <= 0.2:

    workers_low = 0 * np.ones((16))
    for pos in range (0,16):
        if pos == 0 or pos == 1:
            workers_low [pos] = df['workers_low',pos]= gross_area * (1/500)
        elif pos >= 2 and pos <= 12:
            workers_low [pos] = df['workers_low', pos] = gross_area * (1 / 1000)
        elif pos == 13:
            workers_low [pos] = df['workers_low', pos] = 3 * percentage_damaged_low [pos]
        elif pos >= 14:
            workers_low [pos] = df['workers_low', pos] = 2 * percentage_damaged_low [pos]

    downtime_low = df['downtime_low'] = defuzzification_low / workers_low

    repair_time_low = df['repair_time_low'] = downtime_low

    downtime = np.sum(repair_time_low)
    # downtime = repair_time[2]+repair_time[3]

if damage > 0.4 and damage < 0.6:

    workers_medium = 0 * np.ones((16))
    for pos in range(0, 16):
        if pos == 0 or pos == 1:
            workers_medium[pos] = df['workers_medium', pos] = gross_area * (1 / 500)
        elif pos >= 2 and pos <= 12:
            workers_medium[pos] = df['workers_medium', pos] = gross_area * (1 / 1000)
        elif pos == 13:
            workers_medium[pos] = df['workers_medium', pos] = 3 * percentage_damaged_medium[pos]
        elif pos >= 14:
            workers_medium[pos] = df['workers_medium', pos] = 2 * percentage_damaged_medium[pos]

    downtime_medium = df['downtime_medium'] = defuzzification_medium / workers_medium

    repair_time_medium = df['downtime'] = downtime_medium

    downtime = np.sum(repair_time_medium)

if damage >= 0.6:

    workers_high = 0 * np.ones((16))
    for pos in range(0, 16):
        if pos == 0 or pos == 1:
            workers_high[pos] = df['workers_high', pos] = gross_area * (1 / 500)
        elif pos >= 2 and pos <= 12:
            workers_high[pos] = df['workers_high', pos] = gross_area * (1 / 1000)
        elif pos == 13:
            workers_high[pos] = df['workers_high', pos] = 3 * percentage_damaged_high [pos]
        elif pos >= 14:
            workers_high[pos] = df['workers_high', pos] = 2 * percentage_damaged_high[pos]

    downtime_high = df['downtime_high'] = defuzzification_high / workers_high

    repair_time_high = df['downtime'] = downtime_high

    downtime = np.sum(repair_time_high)

print(downtime)












