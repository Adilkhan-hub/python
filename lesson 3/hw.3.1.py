def div():
    devidend = int(input("Enter the devidend: "))
    devider = int(input("Enter the devider: "))
    if devider == 0:
        print("You can't use zero as a devider!")
    result = devidend / devider
    print(result)


(div())
