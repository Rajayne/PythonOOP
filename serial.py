"""Python serial number generator."""

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
    def __init__(self, start, base=-1):
        self.start = start
        self.base = base
    def generate(self):
        self.base += 1
        return self.start + self.base
    def reset(self):
        self.start = 100
        self.base = -1