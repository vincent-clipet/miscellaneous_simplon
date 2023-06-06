import math


class BinaryTree:
    

    
    def __init__(self, array:list[object]):
        """Creates a binary tree

        Args:
            array (list[object]): An array of arbitrary values, or 'None' to create an empty tree
        """
        if array is None:
            array = []
        self.build_from(array)

    def build_from(self, array: list[object]):
        """Build/rebuild a binary tree from

        Args:
            array (list[object]): A list of arbitrary values to insert into the tree
        """
        self.array = []
        for i in array:
            self.insert(i)




    def parent_index(self, index: int) -> int:
        """Get the index of this node's parent

        Args:
            index (int): index of the child

        Returns:
            int: index of the parent
        """
        if index == 0: return None
        return math.floor((index - 1)/2)

    def parent(self, index: int) -> object:
        """Get the value of this node's parent

        Args:
            index (int): index of the child

        Returns:
            object: value of the parent
        """
        tmp = self.parent_index(index)
        if tmp == 0: return None
        return self.array[tmp]



    def child_left_index(self, index: int) -> int:
        """Get the index of this node's left child

        Args:
            index (int): index of the parent

        Returns:
            int: index of the left child
        """
        return 2*index+1

    def child_left(self, index: int) -> object:
        """Get this node's left child

        Args:
            index (int): index of the parent

        Returns:
            object: index of the left child
        """
        return self.array[self.child_left_index(index)]



    def child_right_index(self, index: int) -> int:
        """Get the index of this node's right child

        Args:
            index (int): index of the parent

        Returns:
            int: index of the right child
        """
        return 2*index+2

    def child_right(self, index: int) -> object:
        """Get this node's right child

        Args:
            index (int): index of the parent

        Returns:
            object: index of the right child
        """
        return self.array[self.child_right_index(index)]


    
    def is_leaf(self, index: int) -> bool:
        """Is the given index a leaf ?

        Args:
            index (int): index to check

        Returns:
            bool: true if this is a leaf
        """
        return index >= math.floor(len(self.array)/2)
    


    def swap(self, index_a: int, index_b: int):
        """Swap 2 elements in the tree

        Args:
            index_a (int): index of element a
            index_b (int): index of element b
        """
        self.array[index_a], self.array[index_b] = self.array[index_b], self.array[index_a]



    def insert(self, element: object):
        """Insert a value at the end of the tree

        Args:
            element (object): value to insert
        """
        self.array.append(element)

    def insert_at(self, element: object, index: int):
        """Insert a value at a specifix index

        Args:
            element (object): value to insert
            index (int): index where to insert value
        """
        self.array.insert(index, element)


    
    def print(self):
        print(self.array)