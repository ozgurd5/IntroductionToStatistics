# Average, Mod, Median and Quartile of Classed Series

from prettytable import PrettyTable
import statistics as st
import numpy as np

# ANSWER 1
bins_1 = [40, 50, 60, 70, 80, 90, 100]
frequencies_1 = [3, 5, 11, 22, 15, 6]

table_1 = PrettyTable()
table_1.add_column("Class", [f"[{bins_1[i]}, {bins_1[i + 1]})" for i in range(len(bins_1) - 1)])
table_1.add_column("Frequency", frequencies_1)
midpoints = [bins_1[i] + 5 for i in range(len(bins_1) - 1)]
table_1.add_column("Midpoint", midpoints)
print(table_1)

total = 0
for i in range(len(frequencies_1)):
    total += frequencies_1[i] * midpoints[i]
print(f"Average of the classes: {total / sum(frequencies_1)}")

l_mode = list.index(frequencies_1, max(frequencies_1)) * 10 + bins_1[0]
delta_1 = max(frequencies_1) - frequencies_1[list.index(frequencies_1, max(frequencies_1)) - 1]
delta_2 = max(frequencies_1) - frequencies_1[list.index(frequencies_1, max(frequencies_1)) + 1]
print(f"Mode of the classes: {l_mode + (delta_1 / (delta_1 + delta_2)) * 10}")

l_median = int(st.median(range(40, 100)) / 10) * 10
f_1 = np.cumsum(frequencies_1)[int(l_median / 10) - int(bins_1[0] / 10) - 1]
f_med = frequencies_1[int(l_median / 10) - int(bins_1[0] / 10)]
print(f"Median of the classes: {l_median + (((sum(frequencies_1) / 2) - f_1) / f_med) * 10}")

# ANSWER 2
bins_2 = [0, 20, 40, 60, 80, 100]
frequencies_2 = [8, 12, 25, 15, 10]

table_2 = PrettyTable()
table_2.add_column("Class", [f"[{bins_2[i]}, {bins_2[i + 1]})" for i in range(len(bins_2) - 1)])
table_2.add_column("Frequency", frequencies_2)
cumulative_frequencies_2 = np.cumsum(frequencies_2)
table_2.add_column("Cumulative Frequency", cumulative_frequencies_2)
print(table_2)

quartile_1 = sum(frequencies_2) / 4
counter_1 = 0
while quartile_1 > cumulative_frequencies_2[counter_1]:
    counter_1 += 1
l_quartile_1 = bins_2[counter_1]
f1_1 = cumulative_frequencies_2[counter_1 - 1]
print(f"Quartile 1 of the classes: {l_quartile_1} + ( ( ({cumulative_frequencies_2[-1]} / 4) - {f1_1} ) / {frequencies_2[counter_1]} ) * 20 "
      f"= {l_quartile_1 + (((cumulative_frequencies_2[-1] / 4) - f1_1) / frequencies_2[counter_1])}")

quartile_2 = sum(frequencies_2) / 2
counter_2 = 0
while quartile_2 > cumulative_frequencies_2[counter_2]:
    counter_2 += 1
l_quartile_2 = bins_2[counter_2]
f1_2 = cumulative_frequencies_2[counter_2 - 1]
print(f"Quartile 2 of the classes: {l_quartile_2} + ( ( ({cumulative_frequencies_2[-1]} / 2) - {f1_2} ) / {frequencies_2[counter_2]} ) * 20 "
      f"= {l_quartile_2 + (((cumulative_frequencies_2[-1] / 2) - f1_2) / frequencies_2[counter_2])}")

quartile_3 = (3 * sum(frequencies_2)) / 4
counter_3 = 0
while quartile_3 > cumulative_frequencies_2[counter_3]:
    counter_3 += 1
l_quartile_3 = bins_2[counter_3]
f1_3 = cumulative_frequencies_2[counter_3 - 1]
print(f"Quartile 2 of the classes: {l_quartile_3} + ( ( ( (3 * {cumulative_frequencies_2[-1]}) / 4 ) - {f1_3} ) / {frequencies_2[counter_3]} ) * 20 "
      f"= {l_quartile_3 + ((((3 * cumulative_frequencies_2[-1]) / 2) - f1_3) / frequencies_2[counter_3])}")

# --------- OUTPUTS ----------

# OUTPUT 1
# +-----------+-----------+----------+
# |   Class   | Frequency | Midpoint |
# +-----------+-----------+----------+
# |  [40, 50) |     3     |    45    |
# |  [50, 60) |     5     |    55    |
# |  [60, 70) |     11    |    65    |
# |  [70, 80) |     22    |    75    |
# |  [80, 90) |     15    |    85    |
# | [90, 100) |     6     |    95    |
# +-----------+-----------+----------+
# Average of the classes: 74.51612903225806
# Mode of the classes: 76.11111111111111
# Median of the classes: 80.9090909090909

# OUTPUT 2
# +-----------+-----------+----------------------+
# |   Class   | Frequency | Cumulative Frequency |
# +-----------+-----------+----------------------+
# |  [0, 20)  |     8     |          8           |
# |  [20, 40) |     12    |          20          |
# |  [40, 60) |     25    |          45          |
# |  [60, 80) |     15    |          60          |
# | [80, 100) |     10    |          70          |
# +-----------+-----------+----------------------+
# Quartile 1 of the classes: 20 + ( ( (70 / 4) - 8 ) / 12 ) * 20 = 20.791666666666668
# Quartile 2 of the classes: 40 + ( ( (70 / 2) - 20 ) / 25 ) * 20 = 40.6
# Quartile 2 of the classes: 60 + ( ( ( (3 * 70) / 4 ) - 45 ) / 15 ) * 20 = 64.0
