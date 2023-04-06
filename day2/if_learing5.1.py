if __name__ == '__main__':
    car='audi'
    bool=(car.lower() == 'audi')
    print(bool)

    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')


    age = int('12')
    if age < 4:
        price = 0
    elif age < 18:
        price = 5
    else:
        price = 10
    print("Your admission cost is $" + str(price) + ".")


    # 假设在游戏中刚射杀了一个外星人，请创建一个名为 alien_color 的变量，并将其设置为'green'、'yellow'或'red'。
    # 编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了 5 个点。
    # 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
    alien_color = 'green'
    if alien_color == 'green':
        print("You get 5 points.")
    else:
        print("You get 10 points.")

    requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
          print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")


#     创建一个至少包含 5 个用户名的列表，且其中一个用户名为'admin'。想象你要编写代码，在每位用户登录网站后都打印一条问候消息。 遍历用户名列表，并向每位用户打印一条问候消息
    user_names = ['admin', 'user1', 'user2', 'user3', 'user4']
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + user_name + ", thank you for logging in again.")
    # 在为完成练习 5-8 编写的程序中，添加一条 if 语句，检查用户名列表是否为空
    user_names = []
    if user_names:
        for user_name in user_names:
            if user_name == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print("Hello " + user_name + ", thank you for logging in again.")
    else:
        print("We need to find some users!")

    # 在为完成练习 5-10 编写的程序中，执行以下操作：创建一个至少包含 5 个用户名的列表，并将其命名为 current_users。再创建一个包含 5 个用户名的列表，将其命名为 new_users，并确保其中有一两个用户名也包含在列表 current_users 中。
    # 遍历列表 new_users，对于其中的每个用户名，都 检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名未被使用。
    # 确保比较时不区分大消息；换句话说，如果用户名'John'已被使用，应拒绝用户 名'JOHN'
    current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
    new_users = ['admin', 'user1', 'user2', 'user5', 'user6', 'John']
    for new_user in new_users:
        if new_user.lower() in current_users:
            print("Sorry, " + new_user + " is already taken.")
        elif new_user == 'John':
            print("用户名'John'已被使用，应拒绝用户 名'JOHN'")
        else:
            print("Great, " + new_user + " is available.")
#     ：序数表示位置，如 1st 和 2nd。大多数序数都以 th 结尾，只有 1、2 和 3例外
    numbers = list(range(1, 10))
    for number in numbers:
        if number == 1:
            print(str(number) + "st")
        elif number == 2:
            print(str(number) + "nd")
        elif number == 3:
            print(str(number) + "rd")
        else:
            print(str(number) + "th")
