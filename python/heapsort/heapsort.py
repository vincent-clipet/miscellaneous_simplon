import copy
import math


class HeapSort:
    

    
    def __init__(self, list_to_heapify):
        self.build_heap(list_to_heapify)
        self.max_size = len(list_to_heapify)



    def parent_index(self, i):
        if i == 0: return None
        return math.floor((i - 1)/2)

    def parent(self, i):
        if i == 0: return None
        index = math.floor((i - 1)/2)
        return self.heap[index]
    
    def child_left(self, i):
        return self.heap[2*i+1]
    
    def child_left_index(self, i):
        return 2*i+1

    def child_right(self, i):
        return self.heap[2*i+2]
    
    def child_right_index(self, i):
        return 2*i+2
    
    def is_leaf(self, i):
        return i >= math.floor(len(self.heap)/2)
    
    def swap(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

    def swap_custom_index(self, heap, index_a, index_b):
        heap[index_a], heap[index_b] = heap[index_b], heap[index_a]



    def build_heap(self, array):
        # size = len(array)
        self.heap = []
        for i in array:
            self.insert(i)



    def insert(self, element):
        # if len(self.heap) > self.max_size:
        #     return
        self.heap.append(element)

        i = len(self.heap)-1 # get current index
        value = self.heap[i]

        index_parent = self.parent_index(i)
        if index_parent is None: return # first insertion in the list

        while (not i == 0 and self.heap[i] > self.heap[self.parent_index(i)]):
            self.swap(i, self.parent_index(i))
            i = self.parent_index(i)


        
    def heapsort(self):
        max_size = len(self.heap)
        ret = []
        while max_size > 0:
            max_size -= 1
            print("max_size = ", max_size, "  |   old heap => heapsort   |  ", self.heap, " / ", ret)
            self.swap(0, max_size)
            ret.append(self.heap.pop())
            self.heapify(0)
        # swap last 2 values, they are reversed by the heapsort
        ret[-1], ret[-2] = ret[-2], ret[-1]
        self.heap = ret
        self.heap.reverse()



    def heapify(self, index_root):

        # only execute on roots, not orphan leaves
        if not self.is_leaf(index_root):

            index_left = self.child_left_index(index_root)
            index_right = self.child_right_index(index_root)

            if index_left >= len(self.heap) or index_right >= len(self.heap):
                return

            left = self.heap[index_left]
            right = self.heap[index_right]
            root = self.heap[index_root]
            
            # one of the branch is bigger than their root => swappin' time
            if left > root or right > root:
                # left branch bigger than right => swap left with root
                if left > right:
                    self.swap(index_left, index_root)
                    self.heapify(index_left)
                # right branch bigger than left => swap right with root
                else: # right > left
                    self.swap(index_right, index_root)
                    self.heapify(index_right)





#######
# RUN #
#######

values = [9,6,1,4,3,7,2,5,8]
# values = [3,2,1,9]
print("List of values : ", values)

hs = HeapSort(values)
print("Heap : ", hs.heap)
hs.heapsort()
print("Heapsorted : ", hs.heap)