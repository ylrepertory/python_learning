if __name__ == '__main__':
    message = input("Tell me something, and I will repeat it back to you: ")
    print(message)

    name = input("Please enter your name: ")
    print("Hello, " + name + "!")
    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt+="\nWhat is your first name? "
    name = input(prompt)
    print("\nHello, " + name + "!")
    # ：让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
    number = input("Please enter a number: ")
    if int(number) % 10 == 0:
        print("Yes, " + number + " is a multiple of 10.")
    else:
        print("No, " + number + " is not a multiple of 10.")
