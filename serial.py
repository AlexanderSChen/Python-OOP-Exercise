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
    def __init__(self, start = 0):
        """Make a generator with start as the only parameter besides self with default set to 0"""
        self.start = self.next = start

    def __repr__(self):
        """Show the start value and next value"""
        return f"<SerialGenerator start = {self.start} next = {self.next}"

    def generate(self):
        """Return the next number, which is start + 1. Subtracting 1 will not affect the value of self.next, only the returned value."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets the number to the original start"""
        self.next = self.start