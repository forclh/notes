# 第三题：实现链表类


class Node:
    """链表节点"""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """单链表"""

    def __init__(self, data=None):
        self.head = None
        self._length = 0

        if data is not None:
            # 支持列表、元组、集合等可迭代对象
            for value in data:
                self.append(value)

    def traverse(self, callback):
        """遍历链表，对每个节点值调用 callback(index, value)"""
        current = self.head
        index = 0
        while current is not None:
            callback(index, current.value)
            current = current.next
            index += 1

    def append(self, value):
        """在链表尾部添加一个新节点"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self._length += 1

    def prepend(self, value):
        """在链表头部添加一个新节点"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._length += 1

    def insert(self, index, value):
        """在指定索引位置插入新节点，索引从 0 开始"""
        if index < 0 or index > self._length:
            return

        if index == 0:
            self.prepend(value)
            return

        new_node = Node(value)
        current = self.head

        i = 0
        while i < index - 1:
            current = current.next
            i += 1

        new_node.next = current.next
        current.next = new_node
        self._length += 1

    def delete_by_value(self, value):
        """删除第一个值等于 value 的节点，返回是否删除成功"""
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._length -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self._length -= 1
                return True
            current = current.next

        return False

    def delete_by_index(self, index):
        """删除指定索引位置的节点，返回被删除的值，索引越界时返回 None"""
        if index < 0 or index >= self._length:
            return None

        if index == 0:
            value = self.head.value
            self.head = self.head.next
            self._length -= 1
            return value

        current = self.head
        i = 0
        while i < index - 1:
            current = current.next
            i += 1

        value = current.next.value
        current.next = current.next.next
        self._length -= 1
        return value

    def find(self, value):
        """查找值等于 value 的节点，返回其索引，不存在返回 -1"""
        current = self.head
        index = 0

        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return -1

    def get(self, index):
        """获取指定索引位置的值，索引越界时返回 None"""
        if index < 0 or index >= self._length:
            return None

        current = self.head
        i = 0
        while i < index:
            current = current.next
            i += 1

        return current.value

    def get_length(self):
        """返回链表长度"""
        return self._length

    def is_empty(self):
        """判断链表是否为空"""
        return self._length == 0

    def to_list(self):
        """将链表转换为 Python 列表并返回"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __str__(self):
        """返回链表的字符串表示，如 '1 -> 2 -> 3'"""
        values = self.to_list()
        return " -> ".join(str(value) for value in values)


# ============ 测试代码 ============

# 1. 测试从列表初始化
ll = LinkedList([1, 2, 3])
print("初始化链表:", ll)  # 1 -> 2 -> 3

# 2. 测试 append
ll.append(4)
print("append(4)后:", ll)  # 1 -> 2 -> 3 -> 4

# 3. 测试 prepend
ll.prepend(0)
print("prepend(0)后:", ll)  # 0 -> 1 -> 2 -> 3 -> 4

# 4. 测试 insert
ll.insert(2, 99)
print("insert(2, 99)后:", ll)  # 0 -> 1 -> 99 -> 2 -> 3 -> 4

# 5. 测试 get
print("get(0):", ll.get(0))  # 0
print("get(3):", ll.get(3))  # 2
print("get(100):", ll.get(100))  # None

# 6. 测试 find
print("find(99):", ll.find(99))  # 2
print("find(100):", ll.find(100))  # -1

# 7. 测试 get_length
print("长度:", ll.get_length())  # 6

# 8. 测试 is_empty
print("是否为空:", ll.is_empty())  # False

# 9. 测试 to_list
print("转列表:", ll.to_list())  # [0, 1, 99, 2, 3, 4]

# 10. 测试 traverse
result = []
ll.traverse(lambda i, v: result.append((i, v)))
print("遍历结果:", result)  # [(0, 0), (1, 1), (2, 99), (3, 2), (4, 3), (5, 4)]

# 11. 测试 delete_by_value
success = ll.delete_by_value(99)
print("delete_by_value(99):", success, ll)  # True, 0 -> 1 -> 2 -> 3 -> 4

# 12. 测试 delete_by_index
deleted = ll.delete_by_index(0)
print("delete_by_index(0):", deleted, ll)  # 0, 1 -> 2 -> 3 -> 4

# 13. 测试空链表
empty = LinkedList()
print("空链表:", empty)  # (空字符串)
print("空链表长度:", empty.get_length())  # 0
print("空链表是否为空:", empty.is_empty())  # True
