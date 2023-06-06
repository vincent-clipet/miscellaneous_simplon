from __future__ import annotations
import itertools
import math


class Tree:
    

    
    def __init__(self, value):
        self.parent = None
        self.children = []
        self.value = value
    


    @classmethod
    def swap_a_b(cls, a: Tree, b: Tree):
        """Swap 2 nodes. Children get swapped. Parent get swapped, Reference get swapped (useful to update self.parent.children)

        Args:
            a (Tree): node a
            b (Tree): node b
        """
        a.children, b.children = b.children, a.children
        a.parent, b.parent = b.parent, a.parent
        a, b = b, a
    


    def swap(self, a: Tree):
        """Swap with another node. Children get swapped. Parent get swapped. Reference get swapped (useful to update self.parent.children)

        Args:
            a (Tree): node to swap
        """
        self.swap(a, self)



    def add_child(self, child: Tree):
        """Add a new child

        Args:
            child (Tree): child to add
        """
        self.children.append(child)
        child.parent = self


    def add_children(self,  children: list[Tree]):
        """Add a bunch of new children

        Args:
            child (list[Tree]): children to add
        """
        for c in children:
            self.add_child(c) 

    def add_child_at(self, child: Tree, index: int):
        """add a child node at a specific index

        Args:
            child (object): child to add
            index (int): index where to add value
        """
        self.children.insert(index, child)



    def get_traversal_sum(self):
        if self.is_root():
            return self.value
        else:
            return self.value + self.parent.get_traversal_sum()

    def get_nodes_at_depth(self, depth: int) -> list[Tree]:
        ret = []
        if depth == 0: # this node
            ret.append(self)
        else: # this node's children. Enter recursion
            depth -= 1
            for c in self.children:
                ret += c.get_nodes_at_depth(depth)
        return ret

    def get_all_leaves(self):
        if self.is_leaf():
            return [self]
        else:
            ret = list(itertools.chain.from_iterable([c.get_all_leaves() for c in self.children]))
            return ret
        


    def is_leaf(self) -> bool:
        """Is the given index a leaf ?

        Returns:
            bool: true if this is a leaf
        """
        return self.get_children_count() == 0
    
    def is_root(self) -> bool:
        """Is this the root of the tree ?

        Returns:
            bool: true if this is the root
        """
        return self.parent is None
    
    def get_children_count(self) -> int:
        """Get the number of children this Tree has

        Returns:
            int: number of children
        """
        return len(self.children)



    def get_tree_values(self):
        ret = self.get_full_values_chain()
        if len(ret) <= 1:
            return ret
        else:
            ret[0], ret[1] = ret[1], ret[0]
            return ret

    def get_full_values_chain(self):
        ret = []
        ret.append(self.value)
        if self.is_root():
            return ret
        else:
            [ret.append(i) for i in self.parent.get_tree_values()]
        
        ret.reverse()
        return ret
        

    @staticmethod
    def get_tree_list_values(trees: list[Tree]):
        return [t.value for t in trees]



    
    def to_string(self, depth: int):
        ret = ""
        # ret += "    " * (depth - 1)
        ret += str(self.value)
        depth += 1
        for s in self.children:
            ret += "\n"
            ret += "    " * (depth - 1)
            ret += "|- "
            ret += s.to_string(depth)
        return ret
    
    def print(self):
        print(self.to_string(0))

    def to_string(self, depth):
        depth += 1
        ret = ""
        ret += str(self.value) + "\n"
        for c in self.children:
            ret += "   " * (depth-1)
            ret += "├─ "
            ret += c.to_string(depth)
        return ret