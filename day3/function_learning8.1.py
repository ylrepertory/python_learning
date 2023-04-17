
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")




def pet(name, animal='dog'):
    """显示宠物的信息
    param name: 宠物的名字
    param animal: 宠物的类型
    默认值必须放在最后"""
    print("\nI have a " + animal + ".")
    print("My " + animal + "'s name is " + name.title() + ".")

def describe_pet(animal_type, pet_name='willie'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上
# 的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数
def make_shirt(size, words):
    print("The size of the T-shirt is " + size + ", and the words on it are " + words + ".")
if __name__ == '__main__':
    greet_user('jesse')
    pet('dog', 'willie')
    describe_pet( 'hamster', 'harry' )
    make_shirt('L', 'I love Python')

# 编写一个名为 display_message()的函数，它打印一个句子，指出你在本
# 章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print("I'm learning how to write functions.")


display_message()


# 编写一个名为 favorite_book()的函数，其中包含一个名为 title 的形参。
# 这个函数打印一条消息，如 One of my favorite books is Alice in
# Wonderland。调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")


favorite_book('alice in wonderland')

