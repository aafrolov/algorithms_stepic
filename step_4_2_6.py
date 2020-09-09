"""
Задача на программирование: кодирование Хаффмана
"""


def path_finder(_dict, _key):
    cur_key = _key
    path = ''
    while cur_key in _dict.keys():
        path += _dict[cur_key][1]
        cur_key = _dict[cur_key][0]
    return path[::-1]


class Huffman:
    def __init__(self):
        self.data_array = []

    def insert(self, elem):
        self.data_array.append(elem)

    def extract_min(self):
        return self.data_array.pop(self.data_array.index(min(self.data_array, key=lambda min2: min2[1])))


input_data = input()
queue = Huffman()

for ch in input_data:
    new_element = (ch, input_data.count(ch))
    if new_element not in queue.data_array:
        queue.insert(new_element)

graph = dict()

if len(queue.data_array) == 1:
    node0 = queue.extract_min()
    graph[node0[0]] = (node0[0] + '_', '0')

while len(queue.data_array) > 1:
    node0 = queue.extract_min()
    node1 = queue.extract_min()
    queue.insert((node0[0] + node1[0], node0[1] + node1[1]))
    graph[node0[0]] = (node0[0] + node1[0], '0')
    graph[node1[0]] = (node0[0] + node1[0], '1')

codes = dict()
for key in graph.keys():
    if len(key) == 1:
        codes[key] = path_finder(graph, key)

result_str = ''
for i in input_data:
    result_str += codes[i]

print(str(len(codes.keys())) + ' ' + str(len(result_str)))

for key in codes.keys():
    print(key + ": " + codes[key])

print(result_str)


