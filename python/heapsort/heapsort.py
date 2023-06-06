import random
from src.heap import Heap




#######
# RUN #
#######

values = [9,6,1,4,3,7,2,5,8]
print("List of values : ", values) ; heap = Heap(values)
print("Heap : ") ; heap.print()
heap.heapsort(True) ; heap.print()


print("================================================================")
print("================================================================")
print("================================================================")


values = [random.randint(-10,10) for i in range(0,15)]
print("List of values : ", values) ;
heap = Heap(values)
print("Heap : ") ; heap.print()
heap.heapsort(True) ;
print("heapsorted : ") ; heap.print()