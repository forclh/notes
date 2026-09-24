from abc import ABC, abstractmethod


class Sequence(ABC):
    @abstractmethod
    def append(self, item):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass

    def is_empty(self):
        return self.length() == 0


class ListSequence(Sequence):
    def __init__(self):
        self._data = []

    def append(self, item):
        self._data.append(item)

    def get(self, index):
        return self._data[index]

    def length(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListSequence(Sequence):
    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")
        current = self._head
        for _ in range(index):
            current = current.next
        return current.value

    def length(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current.value
            current = current.next


# 使用
list_seq = ListSequence()
list_seq.append(1)
list_seq.append(2)
list_seq.append(3)
print(list_seq.get(1))  # 2
print(list_seq.length())  # 3
print(list(list_seq))  # [1, 2, 3]
print(list_seq.is_empty())  # False

linked_seq = LinkedListSequence()
linked_seq.append("a")
linked_seq.append("b")
linked_seq.append("c")
print(linked_seq.get(1))  # b
print(linked_seq.length())  # 3
print(list(linked_seq))  # ['a', 'b', 'c']
print(linked_seq.is_empty())  # False
