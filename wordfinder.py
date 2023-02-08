"""Word Finder: finds random words from a dictionary."""
import random
class WordFinder:
    """Class to read file and find words
    
    >>> smallWords = WordFinder("words.txt")

    >>> smallWords.read_file()
    
    >>> smallWords.random()
    
    """
    # Class that contains filename and file
    def __init__(self, filename):
        self.filename = filename

    # Assigns value to file on self class
    def read_file(self):
        file = open(self.filename, "r")
        self.allText = file.readlines()
        self.length = len(self.allText)
        # print(f"File read and closed, length of file: {length}")
    
    # Finds random word in file using random module method 
    def random(self):
        random_index = random.randint(0, self.length - 1)
        print("I am attempting to read")
        random_word = self.allText[random_index]
        return random_word.replace("\n", "")