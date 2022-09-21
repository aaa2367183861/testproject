'''
    要会自己创建链表

    删除链表元素：
        思路：如果本节点的下一个节点的值等于要删除的元素，
            就将本节点连接到下一个节点


        例子：
            1-6-2-4 target = 2

            第一次： 1.next = 6   1-6-2-4
            第二次： 6.next = 2   1-6-4

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


def removeElements(head, val):
    # 若head.item = val 则移动head直到不为val
    # 这里是保证开头不为要删除的元素 如果是的话 就一直移动到不是
    while head and head.item == val:
        head = head.next

    # 如果链表为空 则直接返回链表
    if not head:
        return head

    # 如果走过上面所有，就进入下面去连接
    pre = head  # 保存链表头节点
    cur = head.next  # 保存链表下一个节点

    while cur:
        if cur.item == val: # 如果本节点的下一个节点 是要删除的元素
            cur = cur.next  # 将下一个节点 转到下下一个节点
            pre.next = cur  # 将本节点 连接到下一个节点
        else:
            pre = pre.next  # 如果不满足 就将本节点 和 下一个节点 都转到下一个节点
            cur = cur.next

    # 最后返回头节点
    return head


if __name__ == '__main__':
    link = create_linkList([1, 2, 6, 3, 4, 5, 6])  # 链表
    value = 6  # 要删除的元素
    removeElements(link, value)
