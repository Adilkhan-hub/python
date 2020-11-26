def my_func(**kwargs):
    return ' '.join(kwargs.values())


print(my_func(name=input("Enter your name: "), surname=input("Enter your surname: "), age=input("Enter your age: "), city=input("Enter the city you are living now: "), email=input("Enter your email address: ")))
