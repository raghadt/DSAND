import sys

def huffman_encoding(data):
    # print(data)
    if data=="":
        return "",""

    huffman = {}
    tree = {}
    val = '1'
    
    for c in data:
        huffman[c] = huffman.get(c, 0) + 1

    for i in sorted(huffman.items(), key=lambda x: x[1]):
        tree[i[0]] = val
        val = ('0'+str(val))
    

    encoding = ''
    for i in data:
        encoding += str(tree[i])

    return encoding, tree

def huffman_decoding(data,tree):
    huffman = {}
    decoding = ''
    val=''
    
    
    for c in tree:
        huffman[tree[c]] = c
#     print(huffman)

    # print('-------------------')
    for i in data:
        if i=='1':
            val += str(i)
            decoding += huffman[val]
            val=''
        else:
            val = (str(val) + str(i))
    
    return decoding

def wrapper(a_great_sentence):


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    try:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    except:
        print ("The size of the encoded data is: {}\n".format(len(a_great_sentence)))

    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("------------------------------------------------------------------------")

    
if __name__ == "__main__":
    # codes = {}

    a_great_sentence = "The bird is the word"
    wrapper(a_great_sentence)

    a_great_sentence = "aaaaa"
    wrapper(a_great_sentence)

    a_great_sentence = ""
    wrapper(a_great_sentence)
