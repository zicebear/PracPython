# 定义链表
class ListNode:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        ''' 初始化一个链表，使用头结点 '''
        self.head = ListNode()

    def append(self, value):
        ''' 在链表尾部增加一个结点 '''
        node = ListNode(value)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def length(self):
        ''' 获取链表长度 '''
        nums = 0
        cur = self.head
        while cur.next:
            nums += 1
            cur = cur.next
        return nums

    def insert(self, pos, value):
        ''' 在链表中间插入一个结点，位置信息不可以小于零或者大于当前链表长度 '''
        if pos < 0 or self.length() < pos:
            print(f"invalid insert pos")
            return
        node = ListNode(value)
        cur = self.head
        cur_pos = 0
        while cur_pos < pos:
            cur = cur.next
            cur_pos += 1
        cur.next, cur.next.next = node, cur.next



x = LinkedList()
x.append(3)
x.append(4)
print(x.length())
x.insert(1,2)
