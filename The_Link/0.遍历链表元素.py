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


def printLink(li):
    head = li

    while head:
        print(head.item)
        head = head.next


if __name__ == '__main__':
    link = create_linkList([1, 2, 6, 3, 4, 5, 6])  # 链表
    printLink(link)
