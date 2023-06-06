import random
from src.tree import Tree





#######
# RUN #
#######

tree = Tree(random.randint(0, 10))
print("Root : ", tree.print)
print("================================================================")

new_children = [Tree(random.randint(10, 19)) for i in range(0,3)]

    # new_child = Tree(random.randint(10, 19))
tree.add_children(new_children)
for j in range(0, 3):
    new_children_2 = [Tree(random.randint(20, 29)) for i in range(0,3)]
    tree.children[j].add_children(new_children_2)
tree.children[0].children[0].add_children([Tree(random.randint(30, 39)), Tree(random.randint(30, 39))])
tree.print()

print("================================================================")

traversal_sum = tree.children[0].children[0].children[0].get_traversal_sum()
print("traversal sum 'tree[0][0][0]' = ", traversal_sum)

print("================================================================")

nodes_at_2 = tree.get_nodes_at_depth(4)
pass