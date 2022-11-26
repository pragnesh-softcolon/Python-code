# Write a menu-driven python program that performs the following:
# Find the area of circle Find area of a triangle
# Find the area of square and rectangle Find Simple Interest
# Exit .


ch = 0
while (ch != 4 and ch < 4):
    print("1: Find area of Circle")
    print("2: Find are of tringle")
    print("3: Find Simple Interest")
    print("4. Quit")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        rad = input("Enter radius of circle: ")
        radius = float(rad)
        area = 3.14 * radius * radius
        print("\nArea of Circle = %0.2f" % area)

    elif ch == 2:
        side1 = input("Enter length of first side: ")
        side2 = input("Enter length of second side: ")
        side3 = input("Enter length of third side: ")

        a = float(side1)
        b = float(side2)
        c = float(side3)
        s = (a + b + c)/2

        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("\nArea of Triangle = %0.2f" % area)

    elif ch == 3:
        principle = float(input("Enter the principle amount:"))
        time = int(input("Enter the time(years):"))
        rate = float(input("Enter the rate:"))
        simple_interest = (principle*time*rate)/100
        print("\nThe simple interest is:", simple_interest)

    elif ch == 4:
        print("invalid choice")
        exit
