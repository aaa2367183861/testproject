'''
    要会自己创建链表

    反转链表思路：
        先创建一个空，然后遍历链表，每次保留本节点，第一次节点连空，之后每次连上一次的节点

        例子：1-2-3
        第一次  1-null
        第二次  2-1-null
        第三次  3-2-1-null

        重点是如何保留本次节点 然后去连接 然后转到下一个节点

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


def reverseList(head):
    # 这里创建一个空,留着让节点去连接，也就是最后的反转链表
    dummy = None

    # 遍历链表
    while head:
        temp = head  # 保留本次遍历的节点（也可以理解为复制链表，其实是拿到链表的头节点）
        head = temp.next  # 转到下一个节点
        temp.next = dummy  # 将本次节点 连接到空
        dummy = temp  # 更新反转链表

    # 返回反转后的链表
    return dummy


if __name__ == '__main__':
    link = create_linkList([1, 2, 6, 3, 4, 5, 6])  # 链表
    reverseList(link)
