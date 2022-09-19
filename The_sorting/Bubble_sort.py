
'''
    冒泡排序的思想就是：
        两个for循环
        从第一个元素开始 每个元素循环 与下一个元素比大小
        如果 > 就交换位置，如果 < 就去看下一个元素
        例如：
            1 6 3 2
            第一次： 1 3 2 6
            第二次： 1 2 3 6
            第三次： 1 2 3 6
            四个元素 遍历四次
            每个元素遍历 n-1次

    整体来说冒泡排序的算法比较简单 也好懂
'''

lst = [1,6,3,2]

def bubbleSort(lst):
    # 这里开始遍历
    for passnum in range(len(lst) - 1,0,-1):
        # 这里每个元素遍历n-1次
        for i in range(passnum):
            # 这里比较本元素与下一个元素大小
            if lst[i] > lst[i + 1]:
                # 如果大于下一个元素，交换位置
                lst[i],lst[i + 1] = lst[i + 1],lst[i]

    return lst
if __name__ == '__main__':
    print(bubbleSort(lst))