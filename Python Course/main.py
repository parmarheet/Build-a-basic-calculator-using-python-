#calculator program

def add(x,y):
     return x + y 

     def subtract(x , y):
        return x - y 

        def multiply(x, y):
            return x * y

            def divide(x, y):
                if y == 0:
                    return "Error ! Division by zero."
                    return x/y

                    print("select operation:")
                    print("1. Add")
                    print("2. Substract")
                    print("3. Multiply")
                    print("4. Divide")

        while true:
            # Take input from the user 
            choice = input("Enter choice (1/2/3/4/): ")

            #Check if the choice is one of the the options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number:"))
                num1 = float(input("Enter second number:"))

                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")

                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")

                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")    

            # Check if the user wants to perform another calculation
            next_calculation = input("Do you want to do another calculation? (yes/no):")         
            if next-calculation.lower() != "Yes":
                break 
            else: 
                print("invalid input, please choose a valid operation.")





