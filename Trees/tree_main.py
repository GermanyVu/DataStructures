from Tree import Node
import random

bin_tree = Node(12)
bin_tree.insert_node(23)
bin_tree.insert_node(24)
bin_tree.insert_node(8)
bin_tree.insert_node(7)
# bin_tree.print_tree()
data_list = bin_tree.inorder_traversal(bin_tree)
print(data_list)


bin_tree2 = Node(50)
for _ in range(50):
    bin_tree2.insert_node(random.randint(0, 100))
bin_tree2.display()
