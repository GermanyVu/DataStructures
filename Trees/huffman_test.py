import huffman as hf

# #main
# alphabet_soup = ['w', 'h', 'y', 'h', 'y', 'y']
# bin = [1,0,1]
#
# #first test
# heap_object = hf.MinHeap(4)
# heap_object.array[0] = 1
# #print('array',all(heap_object.array== [1,None,None,None] ))
# assert all(heap_object.array== [1,None,None,None] )
#
#
# #second test
# heap_object = hf.MinHeap(4)
# heap_object.resize()
# assert all((heap_object.array) ==([None,None,None,None,None,None,None,None]))
# #print(all((heap_object.array) ==([None,None,None,None,None,None,None,None])))
#
#
# #third test
# heap_object = hf.MinHeap(2)
# node1 = hf.Node(3,'a')
# node2 = hf.Node(1,'v')
# heap_object.array[0] = node1
# heap_object.array[1] = node2
# heap_object.swap(0,1)
# assert all(heap_object.array == [node2,node1])
# #print(all(heap_object.array == [node2,node1]))
#
#
#
# #fourth test
# heap_object = hf.MinHeap(3)
# node1 = hf.Node(3,'a')
# node2 = hf.Node(1,'v')
# node3 = hf.Node(7,'t')
# node4 = hf.Node(2,'u')
# heap_object.insert_node(node1)
# heap_object.insert_node(node2)
# heap_object.insert_node(node3)
# heap_object.insert_node(node4)
# #print((heap_object.array[0].frequency, heap_object.array[1].frequency, heap_object.array[2].frequency))
# assert all(heap_object.array == [node2,node4,node3,node1,None,None])
#
#
# #fifth test
# heap_object = hf.MinHeap(3)
# node1 = hf.Node(3,'a')
# node2 = hf.Node(1,'v')
# node3 = hf.Node(7,'t')
# node4 = hf.Node(5,'u')
# heap_object.insert_node(node1)
# heap_object.insert_node(node2)
# heap_object.insert_node(node3)
# heap_object.insert_node(node4)
#
# root1 = heap_object.pop_node()
# root2 = heap_object.pop_node()
# root3 = heap_object.pop_node()
# assert(root1.frequency == 1)
# assert(root2.frequency == 3)
# #print(heap_object.size)
# #print((heap_object.array[0].frequency))
# assert all(heap_object.array == [node3,None,None,None,None,None])
# #print(root3.letter)
#
#
# #sixth test
# heap_object = hf.MinHeap(3)
# node1 = hf.Node(3,'w')
# node2 = hf.Node(7,'g')
# node3 = hf.Node(5,'h')
# node4 = hf.Node(1,'a')
# my_dict = {'w':3, 'g':7, 'h':5, 'a':1}
# heap_object.heapify(my_dict)
# # print(heap_object.array)
# # print(heap_object)
#
# #encoding test
# heap_object = hf.MinHeap(2)
# letter_list = ['w','w','w','w','w','g','g','g','g','g','g','g']
# root = hf.Node(12)
# node1 = hf.Node(5,'c')
# node2 = hf.Node(7,'g')
#
# root.left = node1
# root.right = node2
#
# heap_object.insert_node(root)
# # print(heap_object.array[0])
# huffman = hf.Huffman(letter_list)
# huffman.encoding(heap_object.array[0],'')
# # print(huffman.bin_dict)
# # print(heap_object)
#
# #bin_tree test
# heap_object = hf.MinHeap(2)
# letter_list = ['w','w','w','w','w','g','g','g','g','g','g','g']
# root = hf.Node(12)
# node1 = hf.Node(5,'c')
# node2 = hf.Node(7,'g')
# root.left = node1
# root.right = node2
#
# heap_object.insert_node(root)
# # print(heap_object.array[0].frequency)
# huffman = hf.Huffman(letter_list)
# huffman.bin_tree( heap_object.array[0])
# # print(huffman.bin_tree_list)
#
#
# #huffing test
# heap_object = hf.MinHeap(2)
# letter_list = ['w','w','w','w','w','g','g','g','g','g','g','g','c', 'c','e','e','e']
# huffman = hf.Huffman(letter_list)
#
# huffman.huffing()
# # print('bin tree' ,huffman.bin_tree_list)
# # print('bin dict' ,huffman.bin_dict)
#
# #write code test
# heap_object = hf.MinHeap(2)
# letter_list = ['w','w','w','w','w','g','g','g','g','g','g','g','c', 'c','e','e','e']
# huffman = hf.Huffman(letter_list)
#
# huffman.huffing()
# huffman.write_code()
#
# #find top test
# root = hf.Node(12)
# node1 = hf.Node(5,'c')
# node2 = hf.Node(7,'g')
# node3 = hf.Node(8,'g')
# node4 = hf.Node(9,'g')
# root.left = node1
# root.right = node2
# node1.parent = root
# node2.parent = root
# node2.left = node3
# node2.right = node4
# node3.parent = node2
# node4.parent = node2
#
# huffman = hf.Huffman(letter_list)
# node4.find_top()
# node4.find_top()
# # print(groot.frequency)
# # assert root == huffman.find_top(node4)
#
# #decode

heap_object = hf.MinHeap(2)
letter_list = [
    "w",
    "w",
    "w",
    "w",
    "w",
    "g",
    "g",
    "g",
    "g",
    "g",
    "g",
    "g",
    "c",
    "c",
    "e",
    "e",
    "e",
]
huffman = hf.Huffman(letter_list)
#
# huffman.huffing()
# print(huffman.bin_tree_list)
# root = huffman.decode()
# print(root.right.right.right.letter)


# read code test
huffman = hf.Huffman()
huffman.read_code()


#
