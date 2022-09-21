'''
    要会自己创建链表

    本题引入了 快慢指针 和 环形链表
     这次的快指针一次走两步

    如何判断链表是环形链表呢：
        先创建快慢指针
        如何去遍历
        如果快慢指针能相遇
        那么说明是一个环形链表

        例子：1-2-3-4    # 3节点 和 4节点 成环
                 |-|

            快指针一次走2步，慢指针一次走3步
            第一次：fast = 1 slow = 1
            第二次：fast = 3 slow = 2
            第三次：fast = 3 slow = 3  相遇 是环形

    可以自己做一个强化版： 找到环形链表的环点（也就是链表在哪个节点成环，上面的例子就是在3节点成环）
                        返回节点的下标索引
'''


# 创建节点类
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# 创建链表函数（将节点按尾部连接在一起）
def create_linkList(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node

    return head


def detectCycle(head):
    # 创建快慢指针
    fast, slow = head, head

    while True:
        if not (fast and fast.next):  # 如果快指针为null，或快指针的下一个节点为null，就说明不是环形链表
            return fast
            # return  # 强化
        # 快指针走2步，慢指针走1步
        fast, slow = fast.next.next, slow.next
        if fast == slow:  # 如果快慢指针相遇，说明是环形链表
            return True
            # break  # 强化



    # 下面的代码为强化，寻找环形链表的成环点,
    # 思路：将快指针指向头节点，遍历直到快慢指针再次相遇，那么快指针则是成环点
    # fast = head  # 将快指针重新指向链表头节点
    # index = 0

    # while fast != slow:
    #     fast, slow = fast.next, slow.next
    #     index += 1
    # return index


if __name__ == '__main__':
    link = create_linkList([1, 2, 6, 3, 4, 5, 6])  # 链表
    detectCycle(link)
