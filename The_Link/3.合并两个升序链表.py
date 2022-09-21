'''

    合并两个有序链表思路：
        注意是有序，所以最后返回的链表是一个升序排列的链表

        先创建一个0节点 然后创建一个游标指向0节点
        然后遍历两个链表
        比较俩个链表本节点的值 然后将小的用游标去连接
        最后 如果某个链表有剩余元素直接用游标去连接

        例子：l1 = 1-2-3  l2 = 4-5-6  游标为0

        第一次：0-1
        第二次：0-1-2
        第三次：0-1-2-3
        第四次：0-1-2-3-4
        第五次：0-1-2-3-4-5
        第六次：0-1-2-3-4-5-6


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


def mergeTwoLists(l1, l2):
    dummy = Node(0)  # 创建0节点
    move = dummy  # 创建游标

    # 遍历两个链表
    while l1 and l2:
        if l1.item <= l2.item:  # 如果第一个链表节点 小于 第二个链表的节点
            move.next = l1  # 游标指向第一个链表节点
            l1 = l1.next  # 指向下一个节点
        else:
            move.next = l2
            l2 = l2.next

    # 某个链表有剩余说明都是大的元素，直接用游标连接
    move.next = l1 if l1 else l2

    # 返回合并好的升序链表
    return dummy.next


if __name__ == '__main__':
    link1 = create_linkList([4, 5, 6])  # 链表1
    link2 = create_linkList([1, 2, 3])  # 链表2
    mergeTwoLists(link1, link2)
