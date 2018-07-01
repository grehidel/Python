while True:
    print("Enter any of the following e.g add:\n Add\n Multiply \n Subtract\n Divide \n Quit")
    user_input=input(":")
    if user_input=="Add":
        #Addition function
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        answer=str(num1+num2)
        print("The sum is: "+answer)
    elif user_input=="Multiply":
        #Multiplication function
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        answer=str(num1*num2)
        print("The priduct is: "+answer)
    elif user_input=="Subtract":
        #Subtraction function
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        answer=str(num1-num2)
        print("The difference is: "+answer)
    elif user_input=="Divide":
        #division function
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))
        answer=str(num1/num2)
        print("The quotient  is: "+answer)
    elif user_input=="Quit":
        break
    else:
        print("Invalid choice")

