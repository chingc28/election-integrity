import utils  # noqa: F401, do not remove if using a Mac

import csv
import matplotlib.pyplot as plt
import random
import math


def ones_and_tens_digit_histogram(numbers):
    '''
    Input:
        a list of numbers.
    Returns:
        a list where the value at index i is the frequency in which digit i
        appeared in the ones place OR the tens place in the input list. This
        returned list will always have 10 numbers (representing the frequency
        of digits 0 - 9).

    For example, given the input list
        [127, 426, 28, 9, 90]
    This function will return
        [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]

    That is, the digit 0 occurred in 20% of the one and tens places; 2 in 30%
    of them; 6, 7, and 8 each in 10% of the ones and tens, and 9 occurred in
    20% of the ones and tens.

    See fraud_detection_tests.py for additional cases.
    '''
    histogram = [0] * 10

    # first fill histogram with counts
    for i in numbers:
        # 1's place
        histogram[i % 10] += 1

        # 10's place
        histogram[i // 10 % 10] += 1

    # normalize over total counts
    for i in range(len(histogram)):
        histogram[i] /= len(numbers) * 2

    return histogram


def extract_election_votes(filename, column_names):
    """
    Returns a list of integers that contains the values in
    each row of the column_names
    """

    list_integers = []

    # Reads CSV file into a dictionary
    # First row of the file serves as dictionary keys
    # Rest of the rows are dictionary values
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            # Removes the comma and quotation mark around the numerical value
            # Then it adds that numerical value to a list
            for names in column_names:
                votes = row[names].replace(',', '')
                votes = votes.replace('"', '')
                votes = int(votes)
                list_integers.append(votes)

    return list_integers


def plot_input_least_digits_histogram(histogram):
    """
    Plots a graph of frequencies of ones and tens digit of the
    histogram of input election data
    """
    ideal_y = [0.1 for i in range(10)]
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    plt.plot(digits, ideal_y, label='ideal')
    plt.plot(digits, histogram, label='iran')
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Distribution of the last two digits in election dataset")
    plt.legend(loc='upper left')
    plt.savefig('election-digits.png')
    # plt.show()


def random_number_generator(size):
    """
    Returns a list of random numbers according to size.
    Size is an integer indicating how many random numbers you want generated
    """

    nums_list = [random.randint(1, 99) for j in range(size)]
    return nums_list


def plot_dist_by_sample_size():
    """
    Plots a graph of histograms based on the size of random numbers
    generated.
    """
    digits = [i for i in range(10)]
    ideal_y = [0.1 for i in range(10)]

    plt.plot(digits, ideal_y, label='ideal')

    # Generates list of random numbers based on
    # each size in the list and plots its histogram
    size_of_nums = [10, 50, 100, 1000, 10000]

    for value in size_of_nums:
        random_list = random_number_generator(value)
        histogram = ones_and_tens_digit_histogram(random_list)
        plt.plot(digits, histogram, label=str(value) + " random numbers")

    plt.xlabel("Frequency")
    plt.ylabel("Digit")
    plt.title("Distribution of last two digits in randomly generated samples")
    plt.legend(loc='upper left')
    plt.savefig("random-digits.png")
    # plt.show()


def mean_squared_error(numbers1, numbers2):
    """
    Returns the mean squared error (MSE) between lines. MSE is a number that
    determines the closeness of 2 lines. Bigger the number, the more
    different the lines. If MSE is 0, the lines are identical.

    To calculate MSE, first find the y-value distance for each point between
    the 2 lines (represented as a list of integers) and squaring it.
    MSE is the result of averaging all those squared values.

    Example

    Argument: mean_squared_error([1, 4, 9], [6, 5, 4])
    Returns: 17.0
    """

    # Finds the difference between each value in list1 and list2
    # The difference is squared and added to the total
    mse_total = 0
    for i in range(len(numbers1)):
        difference = numbers1[i] - numbers2[i]
        mse_total += abs(difference) ** 2

    # Averages the total squared differences
    mse = mse_total / len(numbers1)

    return mse


def calculate_mse_with_uniform(histogram):
    """
    Returns the MSE between a desired histogram and a uniform distribution.
    Uniform distribution is the ideal line where each value is 0.1
    """

    ideal = [0.1 for i in range(10)]
    value = mean_squared_error(histogram, ideal)

    return value


def compare_input_mse_to_samples(iran_mse, number_of_iran_datapoints):
    """
    Prints 3 values: (1) Amount of MSEs larger or equal
    to Iran MSE, (2) Amount of MSEs smaller than Iran MSE, and
    (3) p-value of Iranian election null hypothesis
    """

    # (Change naming related to iran into your desired name)

    # Generate a list of random numbers that is the same size as iran's dataset
    # Calculate MSE between random numbers' histogram and uniform distribution
    # Add this calculated MSE to a list
    # Repeat 10,000 times

    mse_data = []
    for i in range(10000):
        ran_num_list = random_number_generator(number_of_iran_datapoints)
        ran_num_histogram = ones_and_tens_digit_histogram(ran_num_list)
        mse_ten_thous = calculate_mse_with_uniform(ran_num_histogram)
        mse_data.append(mse_ten_thous)

    # Compares the list of MSEs to the Iran MSE
    # Counts how many of the MSEs are (1) bigger than Iran MSE
    # and (2) smaller than Iran MSE
    larger = 0
    smaller = 0
    for i in mse_data:
        if i > iran_mse or math.isclose(i, iran_mse):
            larger += 1
        else:
            smaller += 1

    # Calculates the null hypothesis rejection level
    p_value = larger / 10000

    print("Quantity of MSEs larger than or equal to the 2009 " +
          "Iranian election MSE: " + str(larger))

    print("Quantity of MSEs smaller than the 2009 " +
          "Iranian election MSE: " + str(smaller))

    print("2009 Iranian election null hypothesis " +
          "rejection level p: " + str(p_value))

    return smaller, larger, p_value


def results(smaller, larger, p_value):

    """
    Output paragraph interpreting the result
    """
    comparison = ''
    significance = ''

    if p_value < 0.05:
        comparison = "less"
        significance = "is"
    else:
        comparison = "greater"
        significance = "is not"

    percent = round(p_value * 100, 2)

    likeliness = ''

    if percent < 5:
        likeliness = "highly unlikely"
    elif 5 <= percent < 15:
        likeliness = "unlikely"
    else:
        likeliness = "likely"

    print(f"About {smaller} of random MSEs were smaller " +
          f"than the input election MSE. This means only {larger} random MSEs" +
          f"were larger than the input election MSE. The p-value, {p_value}, " +
          f"is also {comparison} than 0.05, indicating that this {significance}" +
          "is statistically significant value. The p-value translates to" +
          f"the fact that only {percent}% of genuine elections would be as " +
          "different from the uniform distribution as the input elections" +
          f" was. It is {likeliness} that the input election was genuine.")


# The code in this function is executed when this
# file is run as a Python program
def main():

    # Problem 1: Read and clean Iranian election data and
    # Problem 2: Plot the election data

    # (change the name of the iran csv file to your input file.)
    # (change the names of candidates to your desired candidates)
    election_data = extract_election_votes("election-iran-2009.csv",
                                           ["Ahmadinejad", "Rezai",
                                            "Karrubi", "Mousavi"])

    histogram = ones_and_tens_digit_histogram(election_data)
    plot_input_least_digits_histogram(histogram)

    # Problem 3: Plot data of random numbers in different sample sizes

    plt.clf()
    plot_dist_by_sample_size()

    # Problem 5 Part 1: Input's MSE

    election_mse = calculate_mse_with_uniform(histogram)

    print("2009 Iranian election MSE: " + str(election_mse))

    # Problem 5 Part 2: Comparing Input's MSE to sample

    input_size = len(election_data)
    smaller, larger, p_value = compare_input_mse_to_samples(election_mse, input_size)
    results(smaller, larger, p_value)


if __name__ == "__main__":
    main()
