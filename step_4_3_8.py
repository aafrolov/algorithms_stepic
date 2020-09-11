"""
Задача на программирование: очередь с приоритетами
"""

class BinHeap:
    def __init__(self):
        self.data = list()

    def sift_up(self, index):
        if index == 0:
            return

        if self.data[(index - 1) // 2] < self.data[index]:
            self.data[(index - 1) // 2], self.data[index] = self.data[index], self.data[(index - 1) // 2]
            self.sift_up((index - 1) // 2)

    def sift_down(self, index):
        if 2*index + 1 >= len(self.data):
            return

        if 2*index + 2 >= len(self.data):
            if self.data[index] < self.data[2*index + 1]:
                self.data[index], self.data[2 * index + 1] = self.data[2 * index + 1], self.data[index]
            return

        if self.data[2*index + 1] > self.data[2*index + 2] and self.data[2*index + 1] > self.data[index]:
            self.data[index], self.data[2 * index + 1] = self.data[2 * index + 1], self.data[index]
            self.sift_down(2 * index + 1)
        elif self.data[2*index + 2] > self.data[index]:
            self.data[index], self.data[2 * index + 2] = self.data[2 * index + 2], self.data[index]
            self.sift_down(2 * index + 2)

    def insert(self, value):
        self.data.append(value)
        self.sift_up(len(self.data) - 1)

    def extract_max(self):
        if len(self.data) <= 0:
            return None

        return_value = self.data[0]
        if len(self.data) > 1:
            self.data[0] = self.data.pop()
            self.sift_down(0)
        else:
            self.data.pop()

        return return_value


num_of_operations = int(input())
new_heap = BinHeap()

for i in range(num_of_operations):
    input_str = input()
    if len(input_str.split()) == 1:
        print(new_heap.extract_max())
    else:
        new_heap.insert(int(input_str.split()[1]))
