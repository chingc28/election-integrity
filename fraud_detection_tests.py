import fraud_detection as fd
import math


def test_ones_and_tens_digit_histogram():
    # Easy to calculate case: 5 numbers, clean percentages.
    actual = fd.ones_and_tens_digit_histogram([127, 426, 28, 9, 90])
    expected = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])

    # Obscure and hard (by hand) to calculate frequencies
    input = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
             144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    actual = fd.ones_and_tens_digit_histogram(input)
    expected = [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
                0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
                0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
                0.047619047619047616]
    for i in range(len(actual)):
        assert math.isclose(actual[i], expected[i])

# write other test functions here


def test_extract_election_votes():

    # Made my own example file of fake election data
    # Tests for proper formatting of list of integers
    # Tests to see each value under the column name
    # gets added to the list of integers

    assert fd.extract_election_votes("fraud_example.csv",
                                     ["Trump", "Biden"]) == [
        34348, 12343432, 687987, 587987,
        1234987, 3234079, 5234098, 5897123]

    print("extract election votes passed!")


def test_mean_squared_error():

    # Tests for the mean squared error given 2 lists

    assert fd.mean_squared_error([3, 4, 5, 6], [1, 5, 6, 9]) == 3.75
    assert fd.mean_squared_error([1, 2, 3], [10, 20, 30]) == 378
    assert fd.mean_squared_error([1, 1, 1], [1, 1, 1]) == 0
    assert fd.mean_squared_error([1, 4, 9], [6, 5, 4]) == 17

    print("mean squared error passed!")


def main():
    # Execute test functions
    test_ones_and_tens_digit_histogram()
    test_extract_election_votes()
    test_mean_squared_error()
    print("Congrats! All tests passed!")


if __name__ == "__main__":
    main()
