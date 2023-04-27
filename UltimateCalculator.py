import numpy as np
import statistics as st
from prettytable import PrettyTable


# TODO: grouped and simple mix - weighted values in classed - multi mode in classed
# TODO: harmonic and geometric averages in classed
# TODO: integrate skewness and coefficient variation functions - create print function

# TODO pearson: mod formula and median formula with "frequencies = [12, 6, 7, 10, 5, 6, 11, 8, 9, 10]
#   bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]" gives different results

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
        values = [30,41,53,61,68,79,82,88,90,98]
        weights = []  # add weights if necessary

    sum_values = sum(values)
    sorted_values = sorted(values)
    range_ = max(values) - min(values) + 1

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

    # Quartiles
    fq_frequency = max(cumulative_frequencies) / 4
    index = 0  # start from 0 and increase until find the corresponding value group
    while cumulative_frequencies[index] < fq_frequency:
        index += 1
    first_quartile = single_values[index]

    second_quartile = median

    tq_frequency = (3 * max(cumulative_frequencies)) / 4
    index = 0
    while cumulative_frequencies[index] < tq_frequency:
        index += 1
    third_quartile = single_values[index]

    # Deviations
    mean_absolute_deviation = sum([abs(i - average) for i in values]) / len(values)
    variance = sum([(i - average) ** 2 for i in values]) / max(cumulative_frequencies - 1)
    standard_deviation = variance ** 0.5
    coefficient_variation_ = (standard_deviation / average) * 100

    # Skewness
    pearson_skewness = (3 * (average - median)) / standard_deviation
    bowley_skewness = ((third_quartile - second_quartile) - (second_quartile - first_quartile)) / (third_quartile - first_quartile)
    if pearson_skewness > 0:
        skewness = "Positive Asymmetry - Right Skewness"
    elif pearson_skewness < 0:
        skewness = "Negative Asymmetry - Left Skewness"
    else:
        skewness = "Symmetric - No Skewness"

    # Kurtosis
    fourth_moment = sum([(i - average) ** 4 for i in values]) / len(values)
    kurtosis_measure = fourth_moment / variance ** 2
    if kurtosis_measure > 3:
        kurtosis = "High"
    elif kurtosis_measure < 3:
        kurtosis = "Low"
    else:
        kurtosis = "Normal"

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
    print(f"Range of the values: {range_}")

    print(f"Average (weighted) of the values: {average}")
    print(f"Harmonic average of the values: {harmonic}")
    print(f"Geometric average of the values: {geometric}")

    print(f"Mode of the values: {mode}")
    print(f"Median of the values: {median}")

    print(f"First quartile of the values: {first_quartile}")
    print(f"Second quartile of the values: {second_quartile}")
    print(f"Third quartile of the values: {third_quartile}")

    print(f"Mean absolute deviation of the values: {mean_absolute_deviation}")
    print(f"Variance of the values: {variance}")
    print(f"Standard deviation of the values: {standard_deviation}")
    print(f"Coefficient variation of the values: {coefficient_variation_}")

    print(f"Pearson skewness of the values: {pearson_skewness}")
    print(f"Bowley skewness of the values: {bowley_skewness}")
    print(f"Skewness of the values: {skewness}")

    print(f"Kurtosis measure of the values: {kurtosis_measure}")
    print(f"Kurtosis of the values: {kurtosis}")


def classed_series():
    # Enter the values
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    frequencies = [12, 6, 7, 10, 5, 6, 11, 8, 9, 10]
    increase_amount = bins[1] - bins[0]

    # Frequencies and Percentages
    cumulative_frequencies = list(np.cumsum(frequencies))
    percentages = [(frequencies[i] / max(cumulative_frequencies)) * 100 for i in range(len(frequencies))]
    cumulative_percentages = list(np.cumsum(percentages))

    # 3 digits after point
    percentages = [round(i, 3) for i in percentages]
    cumulative_percentages = [round(i, 3) for i in cumulative_percentages]

    # Midpoints and Average
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

    if mode_index == frequencies.index(frequencies[-1]):  # if the mode group is the last group
        delta_2 = max(frequencies)
    else:
        delta_2 = frequencies[mode_index] - frequencies[mode_index + 1]

    mode = l_mode + (delta_1 / (delta_1 + delta_2)) * increase_amount

    # Median
    median_frequency = max(cumulative_frequencies) / 2
    median_index = 0
    while median_frequency > cumulative_frequencies[median_index]:
        median_index += 1
    l_median = bins[median_index]
    f_1 = cumulative_frequencies[median_index - 1]

    median = l_median + (((max(cumulative_frequencies) / 2) - f_1) / frequencies[median_index]) * increase_amount

    # Quartiles
    fq_frequency = max(cumulative_frequencies) / 4
    fq_index = 0
    while fq_frequency > cumulative_frequencies[fq_index]:
        fq_index += 1
    l_fq = bins[fq_index]
    fq_1 = cumulative_frequencies[fq_index - 1]
    first_quartile = l_fq + (((max(cumulative_frequencies) / 4) - fq_1) / frequencies[fq_index]) * increase_amount

    second_quartile = median

    tq_frequency = (3 * max(cumulative_frequencies)) / 4
    tq_index = 0
    while tq_frequency > cumulative_frequencies[tq_index]:
        tq_index += 1
    l_tq = bins[tq_index]
    tq_1 = cumulative_frequencies[tq_index - 1]
    third_quartile = l_tq + (((3 * max(cumulative_frequencies) / 4) - tq_1) / frequencies[tq_index]) * increase_amount

    # Deviations
    mean_average_deviation = sum([frequencies[i] * abs(midpoints[i] - average) for i in range(len(frequencies))]) / max(cumulative_frequencies)
    variance = sum([frequencies[i] * ((midpoints[i] - average) ** 2) for i in range(len(frequencies))]) / (max(cumulative_frequencies) - 1)
    standard_deviation = variance ** 0.5
    coefficient_variation_ = (standard_deviation / average) * 100

    # Skewness
    pearson_skewness = (3 * (average - median)) / standard_deviation
    bowley_skewness = ((third_quartile - second_quartile) - (second_quartile - first_quartile)) / (third_quartile - first_quartile)
    if pearson_skewness > 0:
        skewness = "Positive Asymmetry - Right Skewness"
    elif pearson_skewness < 0:
        skewness = "Negative Asymmetry - Left Skewness"
    else:
        skewness = "Symmetric - No Skewness"

    # Kurtosis
    fourth_moment = sum([frequencies[i] * ((midpoints[i] - average) ** 4) for i in range(len(frequencies))]) / len(frequencies)
    kurtosis_measure = fourth_moment / variance ** 2
    if kurtosis_measure > 3:
        kurtosis = "High"
    elif kurtosis_measure < 3:
        kurtosis = "Low"
    else:
        kurtosis = "Normal"

    # Visualization and Printing
    classed_table = PrettyTable()
    classed_table.add_column("Class", [f"[{bins[i]}, {bins[i + 1]})" for i in range(len(bins) - 1)])
    classed_table.add_column("Frequency", frequencies)
    classed_table.add_column("Percentage", [f"%{i}" for i in percentages])
    classed_table.add_column("Cumulative Frequency", cumulative_frequencies)
    classed_table.add_column("Cumulative Percentage", [f"%{i}" for i in cumulative_percentages])
    classed_table.add_column("Midpoint", midpoints)
    classed_table.add_column("Midpoint x Frequency", midpoints_frequencies)
    print(classed_table)

    print(f"Average of the classes: {average}")
    print(f"Mode of the classes: {mode}")
    print(f"Median of the classes: {median}")

    print(f"First quartile of the classes: {first_quartile}")
    print(f"Second quartile of the classes: {second_quartile}")
    print(f"Third quartile of the classes: {third_quartile}")

    print(f"Mean average deviation of the classes: {mean_average_deviation}")
    print(f"Variance of the classes: {variance}")
    print(f"Standard deviation of the classes: {standard_deviation}")
    print(f"Coefficient variation of the classes: %{coefficient_variation_}")

    print(f"Pearson skewness of the classes: {pearson_skewness}")
    print(f"Bowley skewness of the classes: {bowley_skewness}")
    print(f"Skewness of the classes: {skewness}")

    print(f"Kurtosis measure of the classes: {kurtosis_measure}")
    print(f"Kurtosis of the classes: {kurtosis}")


def coefficient_variation(standard_deviation, average):
    return (standard_deviation / average) * 100


def skewness(average, median, standard_deviation, first_quartile, second_quartile, third_quartile):
    pearson_skewness = (3 * (average - median)) / standard_deviation
    bowley_skewness = ((third_quartile - second_quartile) - (second_quartile - first_quartile)) / (
                third_quartile - first_quartile)
    if pearson_skewness > 0:
        skewness = "Positive Asymmetry - Right Skewness"
    elif pearson_skewness < 0:
        skewness = "Negative Asymmetry - Left Skewness"
    else:
        skewness = "Symmetric - No Skewness"
    return pearson_skewness, bowley_skewness, skewness


classed_series()
