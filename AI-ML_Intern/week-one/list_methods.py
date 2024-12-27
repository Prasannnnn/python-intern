while True:
    a = input("Enter the shape")
    if a == "circle":
        pi = 22/7
        r = float(input("Enter the radius: "))
        print(pi*r**2)
    elif a == "Exit":
        break