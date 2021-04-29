from bitarray import bitarray
table = {}
class node:
    def __init__(self,char,huff, end ,left = None, right = None ):
        self.char = char
        self.left = left
        self.right =right
        self.endnode = end
        self.huff = huff
        self.level = len(huff) 
        


def decode(codes,nodes):
    current = nodes
    print(current.endnode)
    char = ''
    for i in codes:
        if i == False:
            current = current.left 
        if i == True:
            current = current.right
        if current.endnode:
            char += current.char
            current = nodes
    return char
    
codes = bitarray()
key = []
val = []

with open('compressed.bin','rb') as file:
    codes.fromfile(file)
    file.close

with open('table.txt','rt') as file:
    length = int(file.readline())
    for i in range(length):
        key.append(file.readline().replace('\n',''))
    for i in range(length):
        val.append(file.readline().replace('\n',''))

nodes = []
for i in range(length):
    nodes.append(node(key[i],val[i],True))


while len(nodes)>1 :
    nodes = sorted(nodes, key=lambda x: x.level,reverse=True)
    k = nodes[0].huff[:-1]
    for i in nodes[1:]:
        if k == i.huff[:-1]:
            break
    if nodes[0].huff[-1] == "0":
        left = nodes[0]
        right = i
    else:
        left = i
        right = nodes[0]
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(node('',k,False, left = left, right=right))    

print(decode(codes,nodes[0]))



    


