import random



#############
# FUNCTIONS #
#############



def generate_random_numbers(nb: int, min_value: int, max_value: int) -> list[int]:
    return [random.randint(min_value, max_value) for i in range(nb)]

def find_less_than_10_comprehension(l: list[int]) -> list[int]:
    return [iter for iter in l if iter < 10]

def find_less_than_10_loop(l: list[int]) -> list[int]:
    ret = []
    for val in l:
        if val < 10:
            ret.append(val)
    return ret
    


len()





#######
# RUN #
#######

rng = generate_random_numbers(1000, 1, 100)
print(rng)


print("----------------------")
print("find all values < 10 by comprehension")
lt10_comprehension = find_less_than_10_comprehension(rng)
print("Number of values under 10 (comprehension) : ", len(lt10_comprehension))
print(lt10_comprehension)


print("----------------------")
print("find all values < 10 by loop")
lt10_loop = find_less_than_10_loop(rng)
print("Number of values under 10 (loop) : ", len(lt10_loop))
print(lt10_loop)














liste = [x for x in range(5)]
