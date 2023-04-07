import numpy as np

"""
notes: the root index is zero
        for every node with index i the left can be found by 2*i + 1
        for the right it can be found by 2*i + 2
"""


class Heap:
    def __init__(self, start_size):
        self.array = np.empty([start_size], dtype="object")
        self.size = 0

    def resize(self):
        new_size = 2 * len(self.array)
        new_array = np.empty([new_size], dtype="object")
        for ind in range(self.size):
            new_array[index] = self.array[index]

        self.array = new_array.copy()

    def swap(self, index1, index2):
        temp_value = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp_value

    def insert_node(self, node):  # inserts at the bottom
        # index = self.find_empty()
        if self.size >= len(self.array):
            self.array.resize()
        index = self.size
        self.array[index] = node
        self.size += 1
        while index > 0:
            if self.array[index] < self.array[(index - 1) / 2]:
                self.swap(
                    self.array[index], self.array[(index - 1) / 2]
                )  # switchig parent
                index = (index - 1) / 2
            else:
                break

    def pop_node(self):  # removes root and returns it also takes leaf and makes it root
        root = self.array[0]
        index = root
        self.array[0] = self.array[self.size - 1]  # move last value to root
        self.array[self.size - 1] = None  # toss out last value
        self.size -= 1

        while index < self.size:
            if (2 * index + 1) < self.size and (
                2 * index + 2
            ) < self.size:  # check if left and right indices not out of range
                if (
                    self.array[(2 * index + 1)] < self.array[(2 * index + 2)]
                    and self.array[(2 * index + 1)] < self.array[(index)]
                ):
                    self.swap(
                        self.array[(2 * index + 1)], self.array[index]
                    )  # switching left
                    index = 2 * index + 1
                elif (
                    self.array[(2 * index + 1)] > self.array[(2 * index + 2)]
                    and self.array[(2 * index + 2)] < self.array[(index)]
                ):
                    self.swap(
                        self.array[(2 * index + 2)], self.array[index]
                    )  # switching right
                    index = 2 * index + 2
                else:
                    break
            elif (2 * index + 1) < self.size:
                if self.array[(2 * index + 2)] < self.array[(index)]:
                    self.swap(
                        self.array[(2 * index + 1)], self.array[index]
                    )  # switching left
                    index = 2 * index + 1
                else:
                    break

            # maybe need condition for right....
            else:
                break

        return root

    def heapify(self, new_array):
        for value in new_array:
            self.insert_node(value)
        # self.array = self.array[self.array is not np.array(None)]
