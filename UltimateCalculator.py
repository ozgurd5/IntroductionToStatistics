import numpy as np
import statistics as st
from prettytable import PrettyTable

# TODO: grouped and simple mix - weighted values in classed - multi mode in classed
# TODO -not important- harmonic and geometric averages in classed


def grouped_to_simple():  # not the most efficient way
    # Enter the values
    values = [12, 32, 22, 45, 15]
    frequencies = [2, 3, 3, 4, 4]

    has_weights = False  # add weights if necessary and make it true
    weights = []

    new_values = []
    for i in range(len(frequencies)):
        for j in range(frequencies[i]):
            new_values.append(values[i])

    new_weights = []
    if has_weights:
        for i in range(len(frequencies)):
            for j in range(frequencies[i]):
                new_values.append(weights[i])

    return new_values, new_weights


def simple_series():
    # Enter the values above if grouped and make it true
    is_grouped = False
    if is_grouped:
        values, weights = grouped_to_simple()

    # Enter the values here if not grouped
    else:
        values = [12, 11, 23, 11, 12, 34, 12, 11, 23, 17]
        weights = []  # add weights if necessary

    sum_values = sum(values)
    sorted_values = sorted(values)

    single_values = sorted(list(set(values)))  # non-repetitive values for bins
    single_values.append(max(single_values) + 1)  # np.histogram is last inclusive. we want to exclude
    frequencies, bin_x = np.histogram(values, single_values)
    single_values.remove(max(single_values))  # back to normal

    cumulative_frequencies = np.cumsum(frequencies)
    percentage = [(frequencies[i] / max(cumulative_frequencies)) * 100 for i in range(len(frequencies))]
    cumulative_percentages = np.cumsum(percentage)

    average = st.fmean(values)  # add weights as a second parameter if necessary
    harmonic = st.harmonic_mean(values)
    geometric = st.geometric_mean(values)

    mode = st.multimode(values)
    median = st.median(values)

    # Quartile
    quartile_frequency = max(cumulative_frequencies) / 4
    index = 0   # start from 0 and increase until find the corresponding value group
    while cumulative_frequencies[index] < quartile_frequency:
        index += 1
    quartile_1 = single_values[index]

    quartile_2 = median

    quartile_frequency = (3 * max(cumulative_frequencies)) / 4
    index = 0
    while cumulative_frequencies[index] < quartile_frequency:
        index += 1
    quartile_3 = single_values[index]

    # Visualization and Printing
    grouped_table = PrettyTable()
    grouped_table.add_column("Value", single_values)
    grouped_table.add_column("Frequency", frequencies)
    # grouped_table.add_column("Weight", weights)
    grouped_table.add_column("Percentage", percentage)
    grouped_table.add_column("Cumulative Frequency", cumulative_frequencies)
    grouped_table.add_column("Cumulative Percentage", cumulative_percentages)
    print(grouped_table)

    print(f"Sorted values: {sorted_values}")
    print(f"Sum of the values: {sum_values}")

    print(f"Average (weighted) of the values: {average}")
    print(f"Harmonic average of the values: {harmonic}")
    print(f"Geometric average of the values: {geometric}")

    print(f"Mode of the values: {mode}")
    print(f"Median of the values: {median}")

    print(f"Quartile 1 of the values: {quartile_1}")
    print(f"Quartile 2 of the values: {quartile_2}")
    print(f"Quartile 3 of the values: {quartile_3}")


def classed_series():
    # Enter the values
    frequencies = [2, 6, 10, 7, 4, 1]
    bins = [30, 36, 42, 48, 54, 60, 66]
    increase_amount = bins[1] - bins[0]

    cumulative_frequencies = list(np.cumsum(frequencies))
    percentages = [(frequencies[i] / max(cumulative_frequencies)) * 100 for i in range(len(frequencies))]
    cumulative_percentages = list(np.cumsum(percentages))

    # 3 digits after point
    percentages = [round(i, 3) for i in percentages]
    cumulative_percentages = [round(i, 3) for i in cumulative_percentages]

    midpoints = [bins[i] + increase_amount / 2 for i in range(len(bins) - 1)]
    midpoints_frequencies = [midpoints[i] * frequencies[i] for i in range(len(midpoints))]
    average = sum(midpoints_frequencies) / max(cumulative_frequencies)

    # Mode
    mode_index = frequencies.index(max(frequencies))
    l_mode = bins[mode_index]

    if mode_index == 0:  # if the mode group is the first group
        delta_1 = max(frequencies)
    else:
        delta_1 = frequencies[mode_index] - frequencies[mode_index - 1]

    if mode_index == frequencies.index(frequencies[-1]):    # if the mode group is the last group
        delta_2 = max(frequencies)
    else:
        delta_2 = frequencies[mode_index] - frequencies[mode_index + 1]

    mode = l_mode + (delta_1 / (delta_1 + delta_2)) * increase_amount

    # Median
    middle_element = max(cumulative_frequencies) / 2
    median_index = 0
    while middle_element > cumulative_frequencies[median_index]:
        median_index += 1
    l_median = bins[median_index]
    f_1 = cumulative_frequencies[median_index - 1]

    median = l_median + (((max(cumulative_frequencies) / 2) - f_1) / frequencies[median_index]) * increase_amount

    # Quartiles
    fq_element = max(cumulative_frequencies) / 4
    fq_index = 0
    while fq_element > cumulative_frequencies[fq_index]:
        fq_index += 1
    l_fq = bins[fq_index]
    fq_1 = cumulative_frequencies[fq_index - 1]

    first_quartile = l_fq + (((max(cumulative_frequencies) / 4) - fq_1) / frequencies[fq_index]) * increase_amount

    second_quartile = median

    tq_element = (3 * max(cumulative_frequencies)) / 4
    tq_index = 0
    while tq_element > cumulative_frequencies[tq_index]:
        tq_index += 1
    l_tq = bins[tq_index]
    tq_1 = cumulative_frequencies[tq_index - 1]

    third_quartile = l_tq + (((3 * max(cumulative_frequencies) / 4) - tq_1) / frequencies[tq_index]) * increase_amount

    # Visualization and Printing
    classed_table = PrettyTable()
    classed_table.add_column("Class", [f"[{bins[i]}, {bins[i + 1]})" for i in range(len(bins) - 1)])
    classed_table.add_column("Frequency", frequencies)
    # classed_table.add_column("Percentage", percentages)
    classed_table.add_column("Cumulative Frequency", cumulative_frequencies)
    # classed_table.add_column("Cumulative Percentage", cumulative_percentages)
    classed_table.add_column("Midpoint", midpoints)
    classed_table.add_column("Midpoint x Frequency", midpoints_frequencies)
    print(classed_table)

    print(f"Average of the classes: {average}")
    print(f"Mode of the classes: {mode}")
    print(f"Median of the classes: {median}")
    print(f"First quartile of the classes: {first_quartile}")
    print(f"Second quartile of the classes: {second_quartile}")
    print(f"Third quartile of the classes: {third_quartile}")


classed_series()
