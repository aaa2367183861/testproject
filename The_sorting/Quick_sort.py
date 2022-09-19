
'''
        这个是最难 也是最快的排序

        快速排序思想：
            默认首个归位的应该是第一个元素

            需要用到left right 去规定范围

            每次归位也是拿其本次列表的第一个元素

            结束条件是 left = right  也就是游标到同一个元素的位置上

            归位（就是用算法去比较他应该在什么地方）：
                拿出每个数 然后去算法将他归位
                在这个已经归位的数的基础上 去将他左边的数 和 右边的数 分别归位

            归位算法：
                先将这个数拿起来
                用while去这个数的左边去找比他大的数 然后把比他大的数放在他的位置 把他放在比他大的数的位置上
                用while去这个数的右边去找比他小的数 然后把比他小的数放在他的位置 把他放在比他小的数的位置上

        例子： 1 102 88 5
        第一次归位：1 102 88 5 --- 1的左边就不用看了 就去看他右边
        第二次归位：1 5 88 102 --- 102就归位了 右边就不用看了
        第三次归位：1 5 88 102 --- 5 就归位了
        第四次归位：1 5 88 102

'''
lst = [1,102,88,5]

def place(lst,left,right):
    # 默认列表第一个元素,拿起这个元素 相当于产生一个空位置
    tmp = lst[left]

    while left < right:
        while left < right and lst[right] >= tmp:   # 从右边找比tmp小的数
            right -= 1                              # 找不到就往左走一步
        lst[left] = lst[right]                      # 将找到的这个元素放到tmp位置

        while left < right and lst[left] <= tmp:    # 从左边找比tmp大的数
            left += 1                               # 找不到就往右走一步
        lst[right] = lst[left]                      # 将找到的这个元素放到tmp位置


    # 最后记得将手里的元素放在空位置上面,最后 left 是等于 right的 所以返回哪个都可以
    lst[left] = tmp
    return left

def QuickSort(lst,left,right):
    if left < right:
        # 要去归位的数
        p = place(lst,left,right)

        # 这里是归位的递归
        QuickSort(lst,left,p - 1)   # 去归位这个数左边的
        QuickSort(lst,p + 1,right)  # 去归位这个数右边的

    return lst

print(QuickSort(lst,0,len(lst) - 1))