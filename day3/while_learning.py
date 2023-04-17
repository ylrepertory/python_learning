if __name__ == '__main__':
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1
    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "
    message = ""
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
            print(message)
    # 使用标志
    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)
    # 使用 break 退出循环
    prompt = "\nPlease enter the name of a city you have visited:"
    prompt += "\n(Enter 'quit' when you are finished.) "
    while True:
        city = input(prompt)
        if city == 'quit':
            break
        else:
            print("I'd love to go to " + city.title() + "!")
    # 在一个循环中使用 continue
    current_number = 0
    while current_number < 10:
        current_number += 1
        if current_number % 2 == 0:
            continue
        print(current_number)
    # 使用 while 循环来处理列表和字典
    #   首先创建一个待验证用户列表
    # 和一个用于存储已验证用户的空列表
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    # 验证每个用户，直到没有未验证用户为止
    # 将每个经过验证的列表都移到已验证用户列表中
    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)

    # 删除包含特定值的所有列表元素
    pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    print(pets)
    while 'cat' in pets:
        pets.remove('cat')
    print(pets)

    # 使用用户输入来填充字典
    responses = {}
    # 设置一个标志，指出调查是否继续
    polling_active = True
    while polling_active:
        # 提示输入被调查者的名字和回答
        name = input("\nWhat is your name? ")
        response = input("Which mountain would you like to climb someday? ")
        # 将答案存储在字典中
        responses[name] = response
        # 看看是否还有人要参与调查
        repeat = input("Would you like to let another person respond? (yes/no) ")
        if repeat == 'no':
            polling_active = False

    print(responses)
