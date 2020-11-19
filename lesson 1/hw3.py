a = input("Enter the digit: ")

while a < "0":
    print("Please enter the number which more than 0")
    a = input("Enter the digit: ")
print(f"{a} + {a + a} + {a + a + a} = {int(a) + int(a + a) + int(a + a + a)}")
