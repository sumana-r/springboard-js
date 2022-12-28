"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self,filename):
        
        self.filename = filename
    def random(self):
       
        file1 = open(self.filename,"r")
        words = [line.rstrip('\n') for line in file1]
        return random.choice(words)

class RandomWordFinder(WordFinder):
    def __init__(self, filename):
        super().__init__(filename)
    def specialword(self):
        file1 = open(self.filename,"r")
        words = [line.rstrip('\n') for line in file1 if line.rstrip() and not line.startswith("#")]
        return words


    

            
       
