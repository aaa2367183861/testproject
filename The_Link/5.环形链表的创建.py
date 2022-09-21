'''
    要会自己创建链表

    创建环形链表
    思路简单：找到成环点，找到尾节点 然后让尾节点指向成环点
'''


# 创建节点类
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

def create_link(li):
    head = Node(li[0])
    tail = head
    for i in li[1:]:
        p = Node(i)
        tail.next = p
        tail = p

    return head

# 创建环形链表
def Circular_Link(li, k):
    '''
    默认成环点与尾节点成环
    :param li: 链表
    :param k: 成环点
    :return: 链表头节点
    '''
    cir_move = li # 成环点
    tail_move = li  # 尾节点
    # 让尾节点指向末尾
    while tail_move.next:
        tail_move = tail_move.next
    # 让成环点指向成环节点
    for i in range(k - 1):
        cir_move = cir_move.next
    # 尾节点指向成环点
    tail_move.next = cir_move

    # 返回头部节点
    return li




if __name__ == '__main__':
    head = create_link([3, 2, 0, -4])
    k = 2
    Circular_Link(head,k)