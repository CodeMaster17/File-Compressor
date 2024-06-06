import heapq

class BinaryTree: 
    def __init__(self,value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __less_than__(self, other):
            return self.freq < other.freq
    
    def __equals__(self, other):
            return self.freq == other.freq

class Huffmancode:

    def __init__(self, path):
        self.path = path
        self.__heap =[]

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
            heapq.heappush(self.__heap, binary_tree_node)


    def __Build_Binary_Tree(self):
        while len(self.__heap) > 1:
            binary_tree_node1 = heapq.heappop(self.__heap)
            binary_tree_node2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node1.freq + binary_tree_node2.freq
            newNode = BinaryTree(None, freq_sum)
            newNode.left = binary_tree_node1
            newNode.right = binary_tree_node2
            # heapq.heappush(self.__heap, newNode)
        return

    def compression(self): 
        # To access the file and extract text from that file
        text  = 'djfndsjnfdsnlfsdlfodskfnsdf' # random text
        frequency_dictionary = self.__frequency_from_text(text)
        # calculate frequency of each text and store it in frequency dictionary
        # create min heap for two minimum frequency
        build_heap = self.__Build_heap(frequency_dictionary)
        # construct binary tree from heap
        self.__Build_Binary_Tree()
        # construct code from binary tree and store it in dictionary
        # construct encoder text.
        # we have return that binary file as an output