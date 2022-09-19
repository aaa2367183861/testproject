
'''

        希尔排序的思想：间隔（也就是元素总数 / 2） range(len(lst) / 2) 记得 间隔是大于0的
            就是在插入排序的思想上面 把元素按间隔(gap) 分开 比较
            间隔每次除2来缩小比较范围

            内核还是插入排序

            例子：1 5 88 3
            第一次：gap = 2 currentvalue = 88 position = 2 --- position = 2 [1 5 88 3]
                  gap = 1 currentvalue = 5 position = 1 --- position 1 [1 5 88 3]
                  gap = 0 ---- (sub = sub / 2 = 1)
            第二次：gap = 1 currentvalue = 5 position = 1 --- position = 1 [1 5 88 3]
                   gap = 1 currentvalue = 88 position = 2 --- position = 2 [1 5 88 3]
                   gap = 1 currentvalue = 3 position = 3 --- position = 2 [1 3 5 88]

            其实就是插入排序 加了个间隔
'''

lst = [1,5,88,3]

def SheelSort(lst):
    sublistcount = len(lst) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            InsertSort(lst,startposition,sublistcount)

        sublistcount = sublistcount // 2

    return lst

def InsertSort(lst,start,gap):
    for index in range(start + gap,len(lst),gap):
        currentvalue = lst[index]
        position = index

        while position >= gap and lst[position - gap] > currentvalue:
            lst[position] = lst[position - gap]
            position = position - gap

        lst[position] = currentvalue

if __name__ == '__main__':

    print(SheelSort(lst))
