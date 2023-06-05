#############
# FUNCTIONS #
#############

def draw_triangle(max_width: int) -> int:
    for iter in range(1, max_width):
        print("*" * iter)


def average_all(*args: list[int]) -> float:
    """Returns the average of all parameters
    ----------
        *args (list[int]): array containing all numbers to average out
    ----------
    Returns:
        float: average
    """
    tmp_sum = sum(list(*args))
    tmp_avg = tmp_sum / len(args)
    return tmp_avg


def sum_all(*args: list[int]) -> int:
    """Returns the sum of all parameters
    ----------
        *args (list[int]): array containing all numbers to average out
    ----------
    Returns:
        int: average
    """
    return sum(list(*args))


def fizz_buzz():
    for iter in range(1, 100):
        s = ""
        if iter % 3 == 0:
            s = "Fizz"
        elif iter % 5 == 0:
            s = "Fuzz"
        else:
            s = str(iter)
        print(s)


def reverse_list(l: list) -> list:
    return l.reverse()

            



#######
# RUN #
#######

draw_triangle(7)

print("===========================================")
a = [1,3,6,9,15,21,65,103]
print("average_all([1,3,6,9,15,21,65,103])")
print(str(average_all(a)))

print("===========================================")
b = [1,2,3,4,5,6,7,8,9,10]
print("sum_all([1,2,3,4,5,6,7,8,9,10])")
print(sum_all(b))

print("===========================================")
fizz_buzz()

print("===========================================")
c = ["A", "B", "C", "F", "I", "Z"]
print("reverse_all(['A', 'B', 'C', 'F', 'I', 'Z'])")
# reversed = reverse_list(c)
reversed = reverse_list(c)
print(str(c))
# print(", ".join(c))