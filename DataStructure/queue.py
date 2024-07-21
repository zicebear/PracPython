# 队列先入先出，python提供了队列方法 collections.deque, 也可以通过列表实现

from collections import deque 

# 使用列表实现
class Queue():
    def __init__(self):
        self.queue = []

    # 队尾插入元素
    def enqueue(self, a):
        self.queue.append(a)

    # 队首删除元素
    def dequeue(self):
        self.queue.pop(0)

    # 查看队首元素
    def peek(self):
        return self.queue[0]

    # 检查队列是否为空
    def is_empty(self):
        return len(self.queue) == 0

    # 获取队列大小
    def size(self):
        return len(self.queue)