Written By Jonathan Richard

Department of Electrical Engineering Universitas Indonesia
# huffmancoding-Python
This repository contains one encode script and one decode script. The encode script will generate the huffman table and export it to table.txt, and encode the following string  and then export it to compressed.bin .The decode function generates the huffman tree from the available huffman table in table.txt, and then proceeds to decode the byte file to the original string. Compatible with C# Huffman Coding code in my repositiory (the encoded file here can be decoded with the C# code, and vice versa.)

# Source code contents
## BitArray Version
This version is much faster but requires the BitArray package acquirable in Pip. Compatible only with Python 3. 
## Standard Version
Slower version, this version could be easily ported into MicroPython (and has been tested before) because it only used standard libraries of python. 

# Usage
### Put your string into string.txt 
### Run Encoder.py
### New files are created: compressed.bin is the encoded string and table.txt contains the huffman table. 
### Run decoder.py and it will print the decoded string into the terminal. 

