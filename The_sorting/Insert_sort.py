
'''

        插入排序的思想：

            一个for 一个while
            for循环 默认第一个元素为最小值(所以是从第二个元素开始循环的)
                    然后保存本次循环的下标(position) 和 元素值(currentvalue)
            while循环 当前元素与之前所有元素比 找出之前所有元素中最大的并将最大元素放在本次for循环元素循环位置
                然后在循环结束后 将本次for循环元素(currentvalue) 放到最大元素位置

            例子：
                1 102 88 5
                第一次: currentvalue = 102 position = 1 --- position = 1   [1 3 88 5]
                第二次：currentvalue = 3 position = 2 --- position = 1   [1 88 102 5]
                第三次：currentvalue = 5 position = 3 --- position = 2   [1 5 88 102]

            其实就相当于你开始 手里拿着一个元素 然后去循环和之前的比较
            发现比你手里大的 就把大的放在手里元素的位置上
            最后 把手里的元素放在空着的位置上
'''

lst = [1,102,88,5]

def InsertSort(lst):
    for index in range(1,len(lst)):
        # 保存本次循环的 值 和 下标
        currentvalue = lst[index]
        position = index

        # 这里注意 position > 0 也要作为一个循环结束的条件
        while position > 0 and lst[position - 1] > currentvalue:
            lst[position] = lst[position - 1]
            position = position - 1

        #  在while循环结束以后 交换元素位置
        lst[position] = currentvalue

    return lst

if __name__ == '__main__':
    print(InsertSort(lst))