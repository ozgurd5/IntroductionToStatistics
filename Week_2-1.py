# Frequency Table and Histogram

import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable

values = [80, 40, 40, 50, 30, 40, 60, 30, 100, 60, 70]
# ANSWER 1
print(f"Sum of values: {sum(values)}")

# ANSWER 2
values.sort()
print(f"Sorted values: {values}")

single_values = list(set(values))   # single_values are non repetitive values
single_values.sort()
single_values.append(max(single_values) + 1)    # only to calculate bin_edges. we won't print that
counts, bins_ = np.histogram(values, single_values)


def default_table():
    print("Value : Frequency")
    print("%-s : %-s" % (5 * "-", 9 * "-"))
    for i in range(len(counts)):
        print("%5d : %-9d" % (single_values[i], counts[i]))


def pyplot_histogram():
    plt.hist(values)
    plt.show()


def pretty_table():
    frequency_table = PrettyTable(["Value", "Frequency"])
    for j in range(len(counts)):
        frequency_table.add_row([single_values[j], counts[j]])
    print(frequency_table)


# CHOOSE FOR ANSWER 3
default_table()
pyplot_histogram()
pretty_table()

# ---------- OUTPUTS ----------

# ANSWER 1 OUTPUT
# Sum of values: 600

# ANSWER 2 OUTPUT
# Sorted values: [30, 30, 40, 40, 40, 50, 60, 60, 70, 80, 100]

# ANSWER 3 - DEFAULT TABLE OUTPUT
# Value : Frequency
# ----- : ---------
#    30 : 2
#    40 : 3
#    50 : 1
#    60 : 2
#    70 : 1
#    80 : 1
#   100 : 1

# ANSWER 3 - PRETTY TABLE OUTPUT
# +-------+-----------+
# | Value | Frequency |
# +-------+-----------+
# |   30  |     2     |
# |   40  |     3     |
# |   50  |     1     |
# |   60  |     2     |
# |   70  |     1     |
# |   80  |     1     |
# |  100  |     1     |
# +-------+-----------+
