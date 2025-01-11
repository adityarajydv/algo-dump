from collections import defaultdict

class Node:
    """Represents a node in the Huffman tree."""
    def __init__(self, char, freq):
        """Initializes a node."""
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Compares two nodes based on frequency."""
        return self.freq < other.freq

class HuffmanCoding:
    """Encapsulates Huffman coding functionality."""

    def __init__(self):
        """Initializes the HuffmanCoding object."""
        self.codes = {}  # Store the Huffman codes
        self.root = None # Store the root of the tree

    def build_huffman_tree(self, text):
        """Builds the Huffman tree."""
        if not text:
            return None

        frequencies = defaultdict(int)
        for char in text:
            frequencies[char] += 1

        nodes = [Node(char, freq) for char, freq in frequencies.items()]

        while len(nodes) > 1:
            nodes.sort()
            node1 = nodes.pop(0)
            node2 = nodes.pop(0)

            merged_node = Node(None, node1.freq + node2.freq)
            merged_node.left = node1
            merged_node.right = node2
            nodes.append(merged_node)

        self.root = nodes[0]
        return self.root

    def build_codes(self, node=None, current_code=""):
        """Builds Huffman codes from the tree. Uses self.root if node is not provided."""
        if node is None:
            node = self.root

        if node is None: # handle edge case if root is None
            return

        if node.char is not None:
            self.codes[node.char] = current_code
            return

        self.build_codes(node.left, current_code + "0")
        self.build_codes(node.right, current_code + "1")

    def encode(self, text):
        """Encodes text using Huffman coding."""
        if not text:
            return ""

        self.root = self.build_huffman_tree(text)
        self.codes = {}
        self.build_codes() #build codes after building tree
        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text

    def decode(self, encoded_text):
        """Decodes encoded text using the Huffman tree."""
        if not encoded_text or self.root is None:
            return ""

        decoded_text = ""
        current_node = self.root
        for bit in encoded_text:
            if bit == "0":
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.char is not None:
                decoded_text += current_node.char
                current_node = self.root

        return decoded_text

# Example usage:
huffman = HuffmanCoding() #create instance of class
text = "NAMASTE"
encoded_text = huffman.encode(text)

print("Original text:", text)
print("Encoded text:", encoded_text)

decoded_text = huffman.decode(encoded_text)
print("Decoded text:", decoded_text)

huffman = HuffmanCoding()
text = "GANESHA"
encoded_text = huffman.encode(text)

print("\nOriginal text:", text)
print("Encoded text:", encoded_text)

decoded_text = huffman.decode(encoded_text)
print("Decoded text:", decoded_text)

huffman = HuffmanCoding()
text = "India is my country"
encoded_text = huffman.encode(text)

print("\nOriginal text:", text)
print("Encoded text:", encoded_text)

decoded_text = huffman.decode(encoded_text)
print("Decoded text:", decoded_text)

huffman = HuffmanCoding()
text = ""
encoded_text = huffman.encode(text)