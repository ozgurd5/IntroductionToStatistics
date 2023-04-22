# Cumulative Frequency and Cumulative Percentage Tables

import pandas as pd
import numpy as np
from prettytable import PrettyTable

values = [12, 13, 17, 21, 24, 24, 26, 27, 27, 30, 32, 35, 37, 38, 41, 43, 44, 46, 53, 58]
bins = [10, 20, 30, 40, 50, 60]


def pandas_table():
    frequencies, bins_ = pd.cut(values, bins=bins, right=False, retbins=True, include_lowest=True)
    main_table = pd.value_counts(frequencies, sort=False).to_frame("Frequency")
    sum_frequency = main_table["Frequency"].sum()
    main_table["Percentage"] = main_table["Frequency"] / sum_frequency * 100
    main_table["Cumulative Frequency"] = main_table["Frequency"].cumsum()
    main_table["Cumulative Percentage"] = (main_table["Frequency"] / sum_frequency * 100).cumsum()
    print(main_table)


def pretty_table():
    counts, bins_ = np.histogram(values, bins)
    table = PrettyTable()

    table.add_column("Class", [f"[{10 * i + 10}, {10 * i + 2 * 10})" for i in range(len(counts))])
    table.add_column("Frequency", counts)
    sum_frequency = counts.sum()
    table.add_column("Percentage", [(counts[i] / sum_frequency) * 100 for i in range(len(counts))])
    cumulative_frequency = [counts.cumsum()[i] for i in range(len(counts))]
    table.add_column("Cumulative Frequency", [cumulative_frequency[i] for i in range(len(counts))])
    table.add_column("Cumulative Percentage", [(cumulative_frequency[i] / sum_frequency) * 100 for i in range(len(counts))])
    print(table)


# CHOOSE FOR ANSWER
pandas_table()
pretty_table()

# --------- OUTPUTS ----------

# PANDAS OUTPUT
#           Frequency  Percentage  Cumulative Frequency  Cumulative Percentage
# [10, 20)          3        15.0                     3                   15.0
# [20, 30)          6        30.0                     9                   45.0
# [30, 40)          5        25.0                    14                   70.0
# [40, 50)          4        20.0                    18                   90.0
# [50, 60)          2        10.0                    20                  100.0

# PRETTY TABLE OUTPUT
# +----------+-----------+------------+----------------------+-----------------------+
# |  Class   | Frequency | Percentage | Cumulative Frequency | Cumulative Percentage |
# +----------+-----------+------------+----------------------+-----------------------+
# | [10, 20) |     3     |    15.0    |          3           |          15.0         |
# | [20, 30) |     6     |    30.0    |          9           |          45.0         |
# | [30, 40) |     5     |    25.0    |          14          |          70.0         |
# | [40, 50) |     4     |    20.0    |          18          |          90.0         |
# | [50, 60) |     2     |    10.0    |          20          |         100.0         |
# +----------+-----------+------------+----------------------+-----------------------+
