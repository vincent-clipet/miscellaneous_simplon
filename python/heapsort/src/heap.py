import copy
import math

from .binary_tree import BinaryTree


class Heap(BinaryTree):
    

    
    def __init__(self, array:list[object]):
        BinaryTree.__init__(self, array)

   

    def insert(self, element: object):
        """Insert a value at the end of the tree

        Args:
            element (object): value to insert
        """
        self.array.append(element)

        i = len(self.array)-1 # get current index
        value = self.array[i]

        index_parent = self.parent_index(i)
        if index_parent is None: return # first insertion in the list

        while (not i == 0 and self.array[i] > self.array[self.parent_index(i)]):
            self.swap(i, self.parent_index(i))
            i = self.parent_index(i)
    
    def insert_at(self, element: object, index: int):
        """Not implemented ! Use 'insert()' instead

        Args:
            element (object): 
            index (int): 

        Raises:
            NotImplementedError:
        """
        raise NotImplementedError("Method not implemented for heap. Use 'insert()' instead")



    def heapify(self, index_root: int):
        """'Heapify' the tree downwards, from a specific index, 

        Args:
            index_root (int): Index of the node from which to start the heapify process
        """
        # only execute on roots, not orphan leaves
        if not self.is_leaf(index_root):

            index_left = self.child_left_index(index_root)
            index_right = self.child_right_index(index_root)

            if index_left >= len(self.array) or index_right >= len(self.array):
                return

            left = self.array[index_left]
            right = self.array[index_right]
            root = self.array[index_root]
            
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
    


    def heapsort(self, verbose: bool):
        """Apply Heapsort algorithm on the tree

        Args:
            verbose (bool): Print state of the heap and the sorted tree after each step
        """
        max_size = len(self.array)
        ret = []
        if bool: print("-----------------------------------------------------")
        while max_size > 0:
            max_size -= 1
            if bool: print("old heap => heapsort   |  ", self.array, " / ", ret)
            self.swap(0, max_size)
            ret.append(self.array.pop())
            self.heapify(0)
        if bool: print("-----------------------------------------------------")
        
        # swap last 2 values, they are reversed by mistake at the end of the heapsort
        ret[-1], ret[-2] = ret[-2], ret[-1]
        self.array = ret
        self.array.reverse()
        