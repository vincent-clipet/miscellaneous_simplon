#############
# FUNCTIONS #
#############

import math


def get_lowest(*args: list[int]) -> int:
    """Returns lowest number from the list
    ----------
    Args:
        *args (list[int]): array containing all numbers to compare
    ----------
    Returns:
        int: lowest number
    """
    return sorted(args)[0]


def multiply_with_absolute(a: int, b: int) -> int:
    """Multiplies the absolute value of 'a * b'
    ----------
    Args:
        a (int): value a
        b (int): value b
    ----------
    Returns:
        int: absolute value of 'a * b'
    """
    return int(math.fabs(a * b))

def average(*args: list[int]) -> float:
    """Returns the average of all parameters
    ----------
        *args (list[int]): array containing all numbers to average out
    ----------
    Returns:
        float: average
    """
    tmp_sum = sum(list(args))
    tmp_avg = tmp_sum / len(args)
    return tmp_avg




#######
# RUN #
#######

a = [128,16,1024,4]
print("get_lowest([128,16,1024,4])")
print(get_lowest([128,16,1024,4]))


print("multiply_with_absolute(-7, 9)")
print(str(multiply_with_absolute(-7, 9)))


print("average(-7, 9, 4, 45)")
print(str(average(-7, 9, 4, 45)))



