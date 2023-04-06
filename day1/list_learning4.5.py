if __name__ == '__main__':
    # 有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
    # 使用一个 for 循环将该餐馆提供的五种食品都打印出来, 尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
    foods = ('pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream')

    for food in foods:
        print(food)
    # 你的朋友在另一家自助式餐馆中看到了一家不同的自助餐馆，可供选择的食品有不同。请想出三种你喜欢的食品，并将其存储在一个元组中。
    # 在程序中修改这个元组，将其中的两个元素替换成其他食品。想想看你是如何模拟这家餐馆的变化的，打印一系列核实你所修改的元组确实是对的。
    foods = ('pizza', 'falafel', 'carrot1 cake', 'cannoli', 'ice cream')
    print(foods)
    foods[0]='zz'
