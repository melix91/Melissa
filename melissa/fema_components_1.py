
import pandas as pd

import numpy as np

df = pd.read_excel("building_comp.xlsx")

quantity_per_component = df['QPC'].values.tolist()

quantity_50th = df['50thQ'].values.tolist()

percentage_damaged_low = df['%L']. values.tolist()

percentage_damaged_medium = df['%M']. values.tolist()

percentage_damaged_high = df['%H']. values.tolist()

worker_days_low = df['WL'].values.tolist()

worker_days_medium = df['WM'].values.tolist()

worker_days_high = df['WH'].values.tolist()

total_worker_day_low = df['total_worker_day_low'] = df['%L'] * df['WL']

total_worker_day_medium = df['total_worker_day_medium'] = df['%M'] * df['WM']

total_worker_day_high = df['total_worker_day_high'] = df['%H'] * df['WH']


#variabile livello di danno basso (0.2: test_value)
damage_level_low = df['damage_level_low'] = 0.2 * np.ones((16,1))


#variabile livello di danno medio (0.5: test_value)
damage_level_medium = df['damage_level_medium'] = 0.5 * np.ones((16,1))


#variabile livello di danno alto (0.9: test_value)
damage_level_high = df['damage_level_high'] = 0.9 * np.ones((16,1))
#
defuzzification_low = df['defuzzification_L'] = df['total_worker_day_low'] * df['damage_level_low']

defuzzification_medium = df['defuzzification_M'] = df['total_worker_day_medium'] * df['damage_level_medium']

defuzzification_high = df['defuzzification_H'] = df['total_worker_day_high'] * df['damage_level_high']

#variabile gross area (1400: test value)
gross_area = df['gross_area'] = 1400

#variabile damage (0.5 value_test)
damage = 0.8

if damage <= 0.4:

    workers_low = 0 * np.ones((16,1))
    for pos in range (0,15):
        if pos == 0 or pos == 1:
            workers_low [pos] = df['workers_low',pos]= gross_area * (1/500)
        elif pos >= 2 and pos <= 12:
            workers_low [pos] = df['workers_low', pos] = gross_area * (1 / 1000)
        elif pos == 13:
            workers_low [pos] = df['workers_low', pos] = 3 * percentage_damaged_low [pos]
        elif pos >= 14:
            workers_low [pos] = df['workers_low', pos] = 2 * percentage_damaged_low [pos]
    print (workers_low)

if damage > 0.4 and damage < 0.6:

    workers_medium = 0 * np.ones((16, 1))
    for pos in range(0, 15):
        if pos == 0 or pos == 1:
            workers_medium[pos] = df['workers_medium', pos] = gross_area * (1 / 500)
        elif pos >= 2 and pos <= 12:
            workers_medium[pos] = df['workers_medium', pos] = gross_area * (1 / 1000)
        elif pos == 13:
            workers_medium[pos] = df['workers_medium', pos] = 3 * percentage_damaged_medium[pos]
        elif pos >= 14:
            workers_medium[pos] = df['workers_medium', pos] = 2 * percentage_damaged_medium[pos]
    print(workers_medium)

if damage >= 0.6:

    workers_high = 0 * np.ones((16, 1))
    for pos in range(0, 15):
        if pos == 0 or pos == 1:
            workers_high[pos] = df['workers_high', pos] = gross_area * (1 / 500)
        elif pos >= 2 and pos <= 12:
            workers_high[pos] = df['workers_high', pos] = gross_area * (1 / 1000)
        elif pos == 13:
            workers_high[pos] = df['workers_high', pos] = 3 * percentage_damaged_high [pos]
        elif pos >= 14:
            workers_high[pos] = df['workers_high', pos] = 2 * percentage_damaged_high[pos]
    print(workers_high)













