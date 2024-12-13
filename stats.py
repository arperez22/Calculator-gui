from math import sqrt

def mean(data: list[float]) -> float:
    """
    Calculates the mean, or the average, value of a list of floats
    :param data: A list of floats
    :return: The mean of the data
    """

    return sum(data) / len(data)


def median(data: list[float]) -> float:
    """
    Calculates the median value, or the middle value, of a list of floats
    :param data: A list of floats
    :return: The median value of the data
    """

    data = sorted(data)
    n = len(data)

    if n % 2 == 0:
        middle_left = data[n // 2 - 1]
        middle_right = data[n // 2]
        ans = (middle_left + middle_right) / 2
    else:
        ans = data[n // 2]

    return ans


def mode(data: list[float]) -> float:
    """
    Calculates the mode, or the value that appears most frequently, of a list of floats
    :param data: A list of floats
    :return: The mode of the data
    """

    element_count = {key: data.count(key) for key in data}
    return max(element_count)


def range(data: list[float]) -> float:
    """
    Calculates the range, or the distance from the largest value to the smallest value,
    of a list of floats
    :param data: A list of floats
    :return: The range of the data
    """

    return max(data) - min(data)


def variance(data: list[float]) -> float:
    """
    Calculates the variance of a list of floats.  Variance is a measure of
    how spread out a set of data is.
    :param data: A list of floats
    :return: The variance of the data
    """

    sample_mean = mean(data)
    sample_size = len(data)

    squares = [pow(x - sample_mean, 2) for x in data]

    sum_of_squares = sum(squares)

    return sum_of_squares / (sample_size - 1)



def standard_deviation(data: list[float]) -> float:
    """
    Calculates the standard deviation of a list of floats.  Standard deviation is
    a measure of how spread out a set of data is from the mean.
    :param data: A list of floats
    :return: The standard deviation of the data
    """

    return sqrt(variance(data))