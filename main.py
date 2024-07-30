import heapq, os

class BinaryTree: 
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq

class Huffmancode:

    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.code = {}

    def __frequency_from_text(self, text):
        frequency_dict = {}
        for char in text:
            if char not in frequency_dict:
                frequency_dict[char] = 0
            frequency_dict[char] += 1
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
            heapq.heappush(self.__heap, newNode)
        return

    def __Build_Tree_Code_Helper(self, root, current_code):
        if root is None:
            return
        if root.value is not None:
            self.code[root.value] = current_code
            return
        self.__Build_Tree_Code_Helper(root.left, current_code + "0")
        self.__Build_Tree_Code_Helper(root.right, current_code + "1")

    def __Build_Tree_Code(self):
        root = heapq.heappop(self.__heap)
        self.__Build_Tree_Code_Helper(root, "")

    def __Build_Encoded_Text(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.code[char]
        return encoded_text

    def __Build_Paded_Text(self, encoded_text):
        padding = 8 - len(encoded_text) % 8
        for i in range(padding):
            encoded_text += "0"
        padded_info = "{0:08b}".format(padding)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text

    def __Build_Bytes_Array(self, padded_encoded_text):
        array = []
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte, 2))
        return array

    def compression(self):
        print("Compression is in progress...")
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()
            frequency_dictionary = self.__frequency_from_text(text)
            self.__Build_heap(frequency_dictionary)
            self.__Build_Binary_Tree()
            self.__Build_Tree_Code()
            encoded_text = self.__Build_Encoded_Text(text)
            padded_text = self.__Build_Paded_Text(encoded_text)
            bytes_array = self.__Build_Bytes_Array(padded_text)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)

        print("Compression is done")
        return output_path
    
    def decompression(self, input_path):
        print("Decompression is in progress...")
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + "_decompressed" + ".txt"
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                # convert to integer
                byte = ord(byte) 
                # convert to binary
                bits = bin(byte)[2:].rjust(8, '0') 
                bit_string += bits 
                byte = file.read(1)
            # remove padding
            padding_info = bit_string[:8]
            padding = int(padding_info, 2)
            bit_string = bit_string[8:-padding]
            current_code = ""
            decoded_text = ""
            for bit in bit_string:
                current_code += bit
                if current_code in self.code:
                    character = self.code[current_code]
                    decoded_text += character
                    current_code = ""
            output.write(decoded_text)
        print("Decompression is done")
        return

path = input("Enter the file path: ")
h = Huffmancode(path)
h.decompression(path)
