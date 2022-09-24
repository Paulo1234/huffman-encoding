class node():
    def __init__(self, value, frequency, left=None, right=None):
        #example: a, b, c, j, k...
        self.value = value
        #frequency of the value
        self.frequency = frequency
        #the left node
        self.left = left
        #the right node
        self.right = right

        # direction: 0 or 1
        self.index = ''

class stack():
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)

    def pop(self):
        return self.heap.pop()


def print_huffman_tree(node, value=''):
    code = value + str(node.index)
    if node.left:
        print_huffman_tree(node.left, code)
    if node.right:
        print_huffman_tree(node.right, code)
    
    if not node.left and not node.right:
        codes[node.value] = code

    return codes

#dictionary where will be save the encoded characters
codes = dict()

def encoded_message(data, tree):
    encoding_message = []
    for c in data:
        print(tree[c], end=' ')
        encoding_message.append(tree[c])
    
    string = ''.join([str(item) for item in encoding_message])
    return string

text = str(input('Type a text to compress using huffman enconding:\n> '))

characters = []

frequency = []

for i in range(0, len(text)):
    #Increment character frequency, and add to array if not exists
    if characters.count(text[i]) == 0:
        characters.append(text[i])
        frequency.append(1)
    else:
        index_of_character = characters.index(text[i])
        frequency[index_of_character] += 1

nodes = stack()


#create a stack with all nodes
for x in range(0, len(characters)):
    nodes.push(node(characters[x], frequency[x]))

while len(nodes.heap) > 1:
    left = nodes.pop()
    right = nodes.pop()

    left.index = 0
    right.index = 1

    new_node = node(left.value+right.value, left.frequency+right.frequency, left, right)

    nodes.push(new_node)

tree = print_huffman_tree(nodes.heap[0])

encoded = encoded_message(text, tree)