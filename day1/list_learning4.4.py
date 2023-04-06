if __name__ == '__main__':
    # 要输出列表中的前三个元素
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])
    # 要输出列表中的第 2~4 个元素
    print(players[1:4])
    # 要输出列表中的最后三个元素
    print(players[-3:])
    # 没有指定第一个索引，Python将自动从列表开头开始
    print(players[:4])
    # 提取从第3个元素到列表末 尾的所有元素
    print(players[2:])
    #开头到倒数第三个元素之间的所有元素
    print(players[:-3])
    # 复制列表
    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    print("My favorite foods are:")
    print(my_foods)
    #打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素
    print("The first three items in the list are:")
    print(players[:3])
    #打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素
    print("Three items from the middle of the list are:")
    print(players[1:4])