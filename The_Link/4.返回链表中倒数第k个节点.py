'''
    要会自己创建链表

    本题引入了快慢指针

    获取链表中代数第k个节点思路：
        创建 快指针(fast) 和 慢指针(slow)
        让快指针先走k步
        然后去遍历快指针直到 快指针.next = null
        返回的慢指针链表就是倒数第k的节点

    例子： 1-2-3-4-5 k = 2  fast = 1 slow = 1
        快指针走2步 fast = 3  slow = 1
        遍历快指针，当快指针指到5的时候 fast.next = null slow = 3
        返回慢指针


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

def getKthFromEnd(head, k):

    # 创建快慢指针
    fast,slow = head,head

    # 让快指针先走k步
    for i in range(k):
        fast = fast.next

    # 遍历快指针
    while fast:
        # 快指针和慢指针一直走到fast.next = null
        slow = slow.next
        fast = fast.next

    # 返回慢指针链表
    return slow


if __name__ == '__main__':
    link = create_linkList([1, 2, 6, 3, 4, 5, 6])  # 链表
    k = 2
    getKthFromEnd(link,2)