# File Compressor

In this project, Python was used to implement Huffman coding for file compression and decompression. The `BinaryTree` class represents nodes of a binary tree, which is the core structure for encoding characters based on their frequency. The `Huffmancode` class handles the entire process, starting with reading the text from a file, building a frequency dictionary, and creating a min-heap using Python's `heapq` module to efficiently build the binary tree.

Huffman coding works by assigning shorter binary codes to more frequent characters. The project first calculates the frequency of each character and builds the binary tree. Then, it generates binary codes for each character by traversing the tree. The text is encoded into a binary string and padded to make its length a multiple of 8, after which it is converted into bytes for storage in a binary file.

For decompression, the binary file is read back, and the padding is removed. The bit string is then decoded back into the original text using the stored Huffman codes. Python’s file handling, byte manipulation, and tree traversal capabilities are leveraged to perform both compression and decompression efficiently.

This project demonstrates how Python's data structures and libraries, such as `heapq` for heap operations and `os` for file handling, make it easy to build complex algorithms like Huffman coding.
