if __name__ == '__main__':
    # range()函数 生成一个整数序列
    list1 = range(1, 1000)
    for i in list1:
        print(i)
    print(list1)
    print(sum(list1))

    #平方计算
    squares = []
    for value in range(1,11):
        squares.append(value**2)
    print(squares)

    #两个对比可知 list1是一个生成器(方法)，而squares是一个列表

    #列表解析
    squares=[value ** 2 for value in range(1,11)]
    print(squares)

    # 使用一个 for 循环打印数字 1~20
    for value in range(1,21):
        print(value)
    #创建一个列表，其中包含数字 1~1 000 000，再使用一个 for 循环将这些数字打印出来
    list2 = range(1,1000)
    for i in list2:
        print(i)


    list2=[value  for value in range(1,1000)]
    print(list2)

    # 通过给函数 range()指定第三个参数来创建一个列表，其中包含 1~20 的奇数；再使用一个 for 循环将这些数字都打印出来
    list3 = range(1,20,2)
    for i in list3:
        print(i)
    #创建一个列表，其中包含 3~30 内能被 3 整除的数字；再使用一个 for循环将这个列表中的数字都打印出来.
    list4 = range(3,30,3)
    for i in list4:
        print(i)
    #将同一个数字乘三次称为立方。例如，在 Python 中，2 的立方用 2**3表示。请创建一个列表，其中包含前 10 个整数（即 1~10）的立方，再使用一个 for 循环将这些立方数都打印出来
    list5 = range(1,11)
    for i in list5:
        print(i**3)
    # 使用列表解析生成一个列表，其中包含前 10 个整数的立方
    list6 = [value ** 3 for value in range(1,11)]
    print(list6)