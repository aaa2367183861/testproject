

'''

    归并排序思想：
        用到了递归

        每次分割都是按 mid = len(lst) 分成左右两个列表
        就是先把元素列表分成左列表(lefethalf) 右列表(righthalf) 直到左右列表都为单个元素
        然后去比较两元素大小 合并 再看上一层左右列表 比大小
        直到最终两个列表 合并在一起

        用三个游标 l代表左列表游标  r代表右列表游标 k代表大列表游标

        例子：1 102 88 5
        lefthalf1[1 102] righthalf1[88 5]

        lefthalf1[1 102]:
        lefthalf2[1] righthalf2[102]
        lefthalf1[1 102]

        righthalf1[88 5]:
        lefthalf3[88] righthalf3[5]
        righthalf1[5 88]

        lefthalf1[1 102] righthalf1[5 88]

        [1 5 88 102]

        算法比较简单，想法比较难 建议多debug

'''

lst = [1,102,88,5]


def MergeSort(lst):

    if len(lst) > 1:
        mid = len(lst) // 2

        # 分割成左右两列表
        lefthalf = lst[:mid]
        righthalf = lst[mid:]

        # 去递归 得到最小左右列表 然后去比较 分别放入大列表中
        MergeSort(lefthalf)
        MergeSort(righthalf)

        # 三个游标
        l = 0
        r = 0
        k = 0


        while l < len(lefthalf) and r < len(righthalf):
            if lefthalf[l] < righthalf[r]:
                lst[k] = lefthalf[l]
                l = l + 1
            else:
                lst[k] = righthalf[r]
                r = r + 1
            k = k + 1

        # 存在左列表 或者 右列表 其中一个没有元素的情况
        # 所以 下面是将其中有元素的列表全部放进大列表中

        while l < len(lefthalf):
            lst[k] = lefthalf[l]
            l = l + 1
            k = k + 1

        while r < len(righthalf):
            lst[k] = righthalf[r]
            r = r + 1
            k = k + 1


    return lst

if __name__ == '__main__':
    print(MergeSort(lst))





