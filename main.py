import heapq

class BinaryTree: 
    def __init__(self,value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

class Huffmancode:

    def __init__(self, path):
        self.path = path
        self.__heap =[]

    def __less_than__(self, other):
            return self.frequency < other.frequency
    
    def __equals__(self, other):
            return self.frequeny == other.frequency

    def __frequency_from_text(self,text):
        frequency_dict = {}
        for char in  text:
            if char not in frequency_dict:
                frequency_dict[char] = 0 # char -> key, 0 -> value
            frequency_dict[char] +=1
        return frequency_dict
    

    def __Build_heap(self, frequency_dict):
        for key in frequency_dict:
            frequency = frequency_dict[key]
            binary_tree_node = BinaryTree(key, frequency)
            heapq.push(self.__heap, binary_tree_node)


    def compression(self): 
        # To access the file and extract text from that file
        text  = 'djfndsjnfdsnlfsdlfodskfnsdf' # random text
        frequency_dictionary = self.__frequency_from_text(text)
        # calculate frequency of each text and store it in frequency dictionary
        # create min heap for two minimum frequency
        build_heap = self.__Build_heap(frequency_dictionary)
        # construct binary tree from heap
        # construct code from binary tree and store it in dictionary
        # construct encoder text.
        # we have return that binary file as an output