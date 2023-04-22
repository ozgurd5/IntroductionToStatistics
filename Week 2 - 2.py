# Class Frequency Table

import numpy as np
from prettytable import PrettyTable

values = [1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]
start = 1
interval = 2    # Inclusive in both sides:(10-21)(22-34)... is 12

# numpy histogram calculation
if max(values) % interval == 0:
    bins = int(max(values) / interval)
else:
    bins = int(max(values) / interval) + 1

counts, bin_edges = np.histogram(values, bins)
# numpy histogram calculation

class_frequency_table = PrettyTable(["Class", "Frequency"])
for i in range(len(counts)):
    class_frequency_table.add_row([f"{start} - {start + interval - 1}", counts[i]])
    start += interval
class_frequency_table.add_row(["Sum", sum(counts)])
print(class_frequency_table)

# OUTPUT
# +--------+-----------+
# | Class  | Frequency |
# +--------+-----------+
# | 1 - 2  |     2     |
# | 3 - 4  |     5     |
# | 5 - 6  |     3     |
# | 7 - 8  |     2     |
# | 9 - 10 |     3     |
# |  Sum   |     15    |
# +--------+-----------+
