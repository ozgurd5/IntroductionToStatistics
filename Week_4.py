# Average, Mode and Median of Simple, Grouped and Classed Series

import numpy as np
from prettytable import PrettyTable
import statistics as st

# ANSWER 1
values_1 = [24, 26, 20, 18, 24]
average_1 = sum(values_1) / len(values_1)
print(f"Average of the values: {sum(values_1)} / {len(values_1)} = {average_1}")

# ANSWER 2
values_2 = [35, 38, 36, 36, 37, 36, 38, 35, 39, 37]
single_values_2 = sorted(list(set(values_2)))   # single_values are non repetitive values
single_values_2.append(max(single_values_2) + 1)    # only to calculate bins_ because last bin is inclusive
counts_2, bins_ = np.histogram(values_2, single_values_2)
single_values_2.remove(max(single_values_2))    # calculation of bins_ is done

group_table = PrettyTable()
group_table.add_column("Value", single_values_2)
group_table.add_column("Frequency", counts_2)
print(group_table)

average_2 = 0
for i in range(len(single_values_2)):
    average_2 += (single_values_2[i] * counts_2[i]) / sum(counts_2)
print(f"Average of the values: {sum(values_2)} / {len(values_2)} = {average_2}")

# ANSWER 3
frequencies = [12, 6, 4, 2, 1]

class_table = PrettyTable()
class_table.add_column("Class", [f"[{i * 10}, {i * 10 + 10})" for i in range(5)])
class_table.add_column("Frequency", frequencies)
midpoints = [(i * 10 + 10) - 5 for i in range(5)]
class_table.add_column("Midpoint", midpoints)
frequency_midpoint = [frequencies[i] * midpoints[i] for i in range(5)]
class_table.add_column("Frequency x Midpoint", frequency_midpoint)
class_table.add_column("Cumulative Frequency", np.cumsum(frequencies))

total = 0
for i in range(len(frequencies)):
    total += frequencies[i] * midpoints[i]
average_3 = total / sum(frequencies)
class_table.add_row(["Total", f"{sum(frequencies)}", "-", f"{total}", "-"])

print(class_table)
print(f"Average of the classes: {total} / {sum(frequencies)} = {average_3}")

l_mode = list.index(frequencies, max(frequencies)) * 10

if l_mode / 10 == 0:
    delta_1 = max(frequencies)
else:
    delta_1 = max(frequencies) - frequencies[list.index(frequencies, max(frequencies)) - 1]

if l_mode / 10 == len(frequencies) - 1:
    delta_2 = max(frequencies)
else:
    delta_2 = max(frequencies) - frequencies[list.index(frequencies, max(frequencies)) + 1]

print(f"Mode of the classes: {l_mode} + ({delta_1} / ({delta_1} + {delta_2})) * {10} = {l_mode + (delta_1 / (delta_1 + delta_2)) * 10}")

l_median = int(st.median(range(50)) / 10) * 10
f_1 = np.cumsum(frequencies)[int(l_median / 10) - 1]
f_med = frequencies[int(l_median / 10)]

print(f"Median of the classes: {l_median} + ( ( ({sum(frequencies)} / 2) - {f_1} ) / {f_med} ) * 10 = {l_median + (((sum(frequencies) / 2) - f_1) / f_med) * 10}")

# --------- OUTPUTS ----------

# OUTPUT 1
# Average of the values: 112 / 5 = 22.4

# OUTPUT 2
# +-------+-----------+
# | Value | Frequency |
# +-------+-----------+
# |   35  |     2     |
# |   36  |     3     |
# |   37  |     2     |
# |   38  |     2     |
# |   39  |     1     |
# +-------+-----------+
# Average of the values: 367 / 10 = 36.7

# OUTPUT 3
# +----------+-----------+----------+----------------------+----------------------+
# |  Class   | Frequency | Midpoint | Frequency x Midpoint | Cumulative Frequency |
# +----------+-----------+----------+----------------------+----------------------+
# | [0, 10)  |     12    |    5     |          60          |          12          |
# | [10, 20) |     6     |    15    |          90          |          18          |
# | [20, 30) |     4     |    25    |         100          |          22          |
# | [30, 40) |     2     |    35    |          70          |          24          |
# | [40, 50) |     1     |    45    |          45          |          25          |
# |  Total   |     25    |    -     |         365          |          -           |
# +----------+-----------+----------+----------------------+----------------------+
# Average of the classes: 365 / 25 = 14.6
# Mode of the classes: 0 + (12 / (12 + 6)) * 10 = 6.666666666666666
# Median of the classes: 20 + ( ( (25 / 2) - 18 ) / 4 ) * 10 = 6.25
