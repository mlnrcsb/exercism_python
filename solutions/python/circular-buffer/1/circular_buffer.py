class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message

class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.capacity = capacity
        self.available = capacity
        self.first = 0
        self.last = 0
    def read(self):
        if self.available == self.capacity:
            raise BufferEmptyException('Circular buffer is empty')
        value = self.buffer[self.first]
        self.first = (self.first + 1) % self.capacity
        self.available += 1
        return value

    def write(self, data):
        if not self.available:
            raise BufferFullException('Circular buffer is full')
        self.buffer[self.last] = data
        self.last = (self.last + 1) % self.capacity
        self.available -= 1

    def overwrite(self, data):
        if not self.available:
            self.buffer[self.first] = data
            self.first = (self.first + 1) % len(self.buffer)
        else:
            self.write(data)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.available = self.capacity
        self.first = 0
        self.last = 0
