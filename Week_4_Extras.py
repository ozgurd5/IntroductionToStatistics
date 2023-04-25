# Weighted Average, Harmonic Average, Geometric Average, Mode, Median

from prettytable import PrettyTable
from math import log, exp
import statistics as st

# Weighted Average
lectures = ["Calculus", "Statistics", "Introduction to CS", "Linear Algebra", "Technical English"]
grades = [70, 80, 65, 90, 50]
credits_ = [3, 4, 3, 3, 2]

table_1 = PrettyTable(["Lecture", "Grade", "Credit", "Weight"])
total = 0
for i in range(len(lectures)):
    weight = grades[i] * credits_[i]
    table_1.add_row([lectures[i], grades[i], credits_[i], weight])
    total += weight
    weight = 0
print(table_1)
print(f"Weighted Average = {total} / {sum(credits_)} = {total / sum(credits_)}")

print(st.fmean(grades, credits_))

# Harmonic Average
values = [12, 4, 3, 3, 4, 3, 1, 8]
total = 0
for i in range(len(values)):
    total += 1 / values[i]
print(values)
print(f"Harmonic Average = {len(values)} / {total} = {len(values) / total}")

print(st.harmonic_mean(values))

# Geometric Average
total = 0
for i in values:
    total += log(i)
print(values)
print(f"Geometric Average = e^({total} / {len(values)}) = {exp(total / len(values))}")

print(st.geometric_mean(values))

# --------- OUTPUTS ----------

# OUTPUT 1
# +--------------------+-------+--------+--------+
# |      Lecture       | Grade | Credit | Weight |
# +--------------------+-------+--------+--------+
# |      Calculus      |   70  |   3    |  210   |
# |     Statistics     |   80  |   4    |  320   |
# | Introduction to CS |   65  |   3    |  195   |
# |   Linear Algebra   |   90  |   3    |  270   |
# | Technical English  |   50  |   2    |  100   |
# +--------------------+-------+--------+--------+
# Weighted Average = 1095 / 15 = 73.0
# 73.0

# OUTPUT 2
# [12, 4, 3, 3, 4, 3, 1, 8]
# Harmonic Average = 8 / 2.708333333333333 = 2.953846153846154
# 2.953846153846154

# OUTPUT 3
# [12, 4, 3, 3, 4, 3, 1, 8]
# Geometric Average = e^(10.632773779711947 / 8) = 3.77762959804593
# 3.77762959804593
