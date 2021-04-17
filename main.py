import calculatorfunctions as cf
again = "y"
num1, num2 = 0, 0


while again != "n":
    print("------------------------------")
    print("----------CALCULATOR----------")
    print("------------------------------")
    print("----------1. Addition---------")
    print("----------2. Subtraction------")
    print("----------3. Multiplication---")
    print("----------4. Division---------")
    print("----------5. Power------------")
    print("----------6. Exit------------")
    print("------------------------------")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(num1, " + ", num2, " = ", cf.addition(num1, num2))
        again = input("DO YOU WANT TO CONTINUE(y/n) : ")
        again = again.lower()
    elif choice == 2:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(num1, " - ", num2, " = ", cf.subtraction(num1, num2))
        again = input("DO YOU WANT TO CONTINUE(y/n) : ")
        again = again.lower()
    elif choice == 3:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(num1, " * ", num2, " = ", cf.multiplication(num1, num2))
        again = input("DO YOU WANT TO CONTINUE(y/n) : ")
        again = again.lower()
    elif choice == 4:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(num1, " / ", num2, " = ", cf.division(num1, num2))
        again = input("DO YOU WANT TO CONTINUE(y/n) : ")
        again = again.lower()
    elif choice == 5:
        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))
        print(num1, " ^ ", num2, " = ", cf.power(num1, num2))
        again = input("DO YOU WANT TO CONTINUE(y/n) : ")
        again = again.lower()
    else:
        print("INVALID OPERATION.")



