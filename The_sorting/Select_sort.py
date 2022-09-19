
'''

        选择排序的思想：
            选择排序，两个for循环
                    我会用第一个for循环 去告诉他 最大的元素要放在哪（fillsolt）
                            然后第二个循环 去找真正最大元素的下标 (positionOfMax)
                            最后 交换两个位置的元素

            例子： 1 5 88 3
            第一次: fillsolt = 3 positionOfMax = 0    positionOfMax = 2  [1 5 3 88]
            第二次：fillsolt = 2 positionOfMax = 0    positionOfMax = 1  [1 3 5 88]
            第三次：fillsolt = 1 positionOfMax = 0    positionOfMax = 1  [1 3 5 88]

            选择排序 每次循环 只交换一次元素位置

'''

lst = [1,5,88,3]

def SelectSort(lst):
    for fillsolt in range(len(lst) - 1,0,-1):
        # 默认最大元素下标为0
        positionOfMax = 0

        for location in range(1,fillsolt + 1):
            if lst[location] > lst[positionOfMax]:
                positionOfMax = location

        # 最后才交换两元素位置
        lst[fillsolt],lst[positionOfMax] = lst[positionOfMax],lst[fillsolt]

    return lst

if __name__ == '__main__':
    print(SelectSort(lst))