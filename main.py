class Huffmancode:

    def __init__(self, path):
        self.path = path

    def __frequency_from_text(self,text):
        frequency_dict = {}
        for char in  text:
            if char not in frequency_dict:
                frequency_dict[char] = 0 # char -> key, 0 -> value
            frequency_dict[char] +=1
        return frequency_dict


    def compression(self): 
        # To access the file and extract text from that file
        text  = 'djfndsjnfdsnlfsdlfodskfnsdf' # random text
        frequency_dictionary = self.__frequency_from_text(text)

        # calculate frequency of each text and store it in frequency dictionary
        # create min heap for two minimum frequency
        # construct binary tree from heap
        # construct code from binary tree and store it in dictionary
        # construct encoder text.
        # we have return that binary file as an output