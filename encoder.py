with open('string.txt','rt') as file:
    string = file.read()
    print("String asli:\n" + string)

table = {}
class node:
    def __init__(self,char,freq,left=None,right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right =right
        self.huff = ""
    
def generate(node, val =''):
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


def encode(uncompressed,table):
    text = ''
    for a in uncompressed:
        text+= table[a]
    compressed = bytearray(1)
    n = 0
    pos = 7
    for a in text:
        if pos<0:
            compressed.append(0)
            n += 1
            pos = 7
        if a=="1":
            compressed[n] |= 1 << pos
        else:
            compressed[n] &= ~(1<<pos)
        pos -= 1
    
    return compressed



nodes = []  
freq = checkFrequency(string)

i = 0
for x in freq.keys():
    nodes.append(node(x,freq[x]))
while len(nodes) > 1 :
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    left.huff = "0"
    right.huff = "1"
    nodes.append(node('', left.freq+right.freq, left,right))
    nodes.remove(left)
    nodes.remove(right)
    

generate(nodes[0])
hasil = encode(string, table)
with open('compressed.bin','wb') as file:
    print("Hasil akhir : ")
    print(hasil)
    file.write(hasil)
    file.close

with open('table.txt','wt') as file:
    c = str(len(table.keys())) + "\n"
    file.write(c)
    for a in list(table.keys()):
        file.write(str(a) + "\n")
    for i in list(table.keys()):
        file.write(table[i] +"\n")
    file.close

for x in table.keys():
    print(f'char {x} code {table[x]}')