"""Python serial number generator."""
from random import randint
class SerialGenerator:
    
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100

    """
    def __init__(self,start):
        self.start = start
        self.inc_val = start
    def generate(self):
        print(self.inc_val) 
        self.inc_val += 1
    def reset(self):
        self.inc_val =  self.start 

    

        

