if __name__ == '__main__':
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0['color'])

    alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
    print("Original x-position: " + str(alien_0['x_position']))
    # 向右移动外星人
    # 据外星人当前速度决定将其移动多远
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else:
        # 这个外星人的速度一定很快
        x_increment = 3
    # 新位置等于老位置加上增量
    alien_0['x_position'] = alien_0['x_position'] + x_increment
    print("New x-position: " + str(alien_0['x_position']))

    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0)
    del alien_0['points']
    print(alien_0)

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    print("Sarah's favorite language is " +
     favorite_languages['sarah'].title() +
    ".")

    # 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键 first_name、last_name、age 和 city。将存储在该字典中的每项信息都打印出来
    friend = {'first_name':'zhang','last_name':'san','age':18,'city':'beijing'}
    print(friend)

# 使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储
# 在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的
    favorite_numbers = {'zhangsan':1,'lisi':2,'wangwu':3,'zhaoliu':4,'tianqi':5}
    print(favorite_numbers)
    # Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表
    # 遍历字典中的所有键-值对
    # 想出你在前面学过的 5 个编程词汇，将它们用作词汇表中的键，并将它们的含
    # 义作为值存储在词汇表中。
    # 遍历词汇表，并将 Python 术语及其含义都打印出来
    vocabulary = {'list':'列表','tuple':'元组','dictionary':'字典','if':'条件语句','for':'循环语句'}
    for key,value in vocabulary.items():
        print(key+":"+value)
    #q:不知道这种方式 怎么才能知道？像java在idea中可以看到
    #a:在pycharm中，可以在for循环中输入key，然后按ctrl+alt+v，就会自动创建value
    for key,value in vocabulary.items():
        print(key)
        print(value)
    #     遍历词汇表中的所有键
    #q:这个怎么提前知道返回的是个list?类似java的返回类

    #q:value一般写代码的时候不会混淆吗？没有作用阈也不用定义，会不会出现写着写着用错了
    for name in sorted(favorite_languages.keys()):
        print(name.title() + ", thank you for taking the poll."+value)

    # 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中
    # 以完成以下任务：对于这些人中的每个人，都打印一条消息，指出他是否已经参与了调查。
    survey_list = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', 'jack': 'java', 'tom': 'python'}
    for name in survey_list.keys():
        if name in favorite_languages.keys():
            print(name.title() + ", thank you for taking the poll.")
        else:
            print(name.title() + ", please take the poll.")
    #创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为 pets 的列表中，再遍历该列表，并将宠物的所有信息都打印出来
    pets = [{'name':'tom','type':'cat','master':'zhangsan'},{'name':'jerry','type':'mouse','master':'lisi'}]
    for pet in pets:
        print(pet)

