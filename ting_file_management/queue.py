class Queue:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not bool(self._data):
            return None
        value = self._data[0]
        self._data = self._data[1:]
        return value

    def search(self, index):
        if type(index) is not int or index < 0 or index >= len(self._data):
            raise IndexError
        return self._data[index]
