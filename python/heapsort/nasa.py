import copy
import random
import time
from src.tree import Tree



##########
# CONFIG #
##########

SPOTS_TO_VISIT = 4
MIN_DISTANCE = 10
MAX_DISTANCE = 30



#############
# FUNCTIONS #
#############

def generate_children(root: Tree, max_depth, all_numbers):
    max_depth -= 1
    for i in all_numbers:
        possible_numbers = copy.deepcopy(all_numbers)
        possible_numbers.remove(i)
        new_node = Tree(i)
        root.add_child(new_node)
        if max_depth == 0:
            return
        else:
            generate_children(new_node, max_depth, possible_numbers)

def generate_pathing_cost(paths: int, min: int, max: int) -> list[list[int]]:
    # create 2-dimensional array full of 'None'
    ret = []
    for y in range(0, paths):
        ret.append([None for _ in range(0, paths)])

    for y in range(0, paths):
        costs = []
        for x in range(0, paths):
            if x == y:
                costs.append(0)
            else:
                existing_value = ret[x][y]
                # this pathing cost does not exist, create it
                if (existing_value is None):
                    costs.append(random.randint(min, max))
                # this pathing cost already exists elsewhere, copy it here
                else:
                    costs.append(existing_value)
        ret[y] = costs
    return ret

    



#######
# RUN #
#######

time_start = time.time()

tree = Tree(0)
possible_values = [i for i in range(1,SPOTS_TO_VISIT+1)]
generate_children(tree, len(possible_values), possible_values)
time_build_tree = time.time()
print("[debug] Root : ") ; tree.print()
time_print_root = time.time()
print("================================================================")

# traversal_sum = tree.children[0].children[0].children[0].get_traversal_sum()
# print("[debug] traversal sum 'tree[0][0][0]' = ", traversal_sum)

pathing_costs = generate_pathing_cost(len(possible_values)+1, MIN_DISTANCE, MAX_DISTANCE)
time_pathing_costs = time.time()
print("[debug] Pathing costs : ", pathing_costs)

# nodes_at_depth_2 = tree.get_nodes_at_depth(2)
# print("[debug] nodes_at_depth(2) : ", Tree.get_tree_list_values(nodes_at_depth_2))

# all_leaves = tree.get_all_leaves()
# print("[debug] get_all_leaves : ", Tree.get_tree_list_values(all_leaves))



print("================================================================")



nodes_at_depth = tree.get_nodes_at_depth(SPOTS_TO_VISIT)
time_nodes_at_depth = time.time()
print("nodes_at_depth(SPOTS_TO_VISIT) : ", Tree.get_tree_list_values(nodes_at_depth))

leaderboard = []
for node in nodes_at_depth:
    chain = node.get_tree_values()
    sum = 0
    previous_value = None
    
    for i in chain:
        if previous_value is None:
            previous_value = i
        else:
            sum += pathing_costs[previous_value][i]
            previous_value = i
    leaderboard.append((sum, node, chain))


best_path = min(leaderboard, key = lambda t: t[0])
time_best_path = time.time()
print("Best path = ", best_path[0])

print("Full path : ", best_path[2])
print()
print("-------------------------")

print("Timers for SPOTS_TO_VISIT =", SPOTS_TO_VISIT, ":")

print("-- build tree | ", round(time_build_tree - time_start, 2), " sec")
print("-- print root graph | ", round(time_print_root - time_build_tree, 2), " sec")
print("-- calculate pathing costs | ", round(time_pathing_costs - time_print_root, 2), " sec")
print("-- get nodes at depth 'n' | ", round(time_nodes_at_depth - time_pathing_costs, 2), " sec")
print("-- find best path | ", round(time_best_path - time_pathing_costs, 2), " sec")
print()