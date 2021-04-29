from bitarray import bitarray
import sys
string = "aaaaaaaaaabbbbbccdef"

table = {}
class node:
    def __init__(self,char,freq,left=None,right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right =right
        self.huff = bitarray()
    
def generate(node, val = bitarray()):
    global table
    val = val + node.huff
    if(node.left):
        generate(node.left,val)
    if(node.right):
        generate(node.right,val) 
    if(not node.left and not node.right):
        table[node.char] = val



def checkFrequency(string):
    freq ={}
    for a in string:
        if a in freq:
            freq[a]+= 1
        else:
            freq[a] = 1
    return freq


def encode(string,d):
    newstring = bitarray()
    for a in string:
        newstring += d[a]
    return newstring 



nodes = []  
freq = checkFrequency(string)
i = 0
for x in freq.keys():
    nodes.append(node(x,freq[x]))
while len(nodes) > 1 :
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]

    left.huff.append(False)
    right.huff.append(True)

    newNode = node(left.char+right.char, left.freq+right.freq, left,right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

generate(nodes[0])
hasil = encode(string, table)
with open('compressed.bin','wb') as file:
    hasil.tofile(file)
    file.close

with open('table.txt','wt') as file:
    c = str(len(table.keys())) + "\n"
    file.write(c)
    for a in list(table.keys()):
        file.write(str(a) + "\n")
    for i in list(table.keys()):
        table[i] = table[i].to01() + "\n"
        file.write(table[i])
    file.close
print(table)