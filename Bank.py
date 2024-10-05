print("="*20)

customerNames = ['Jane Smith', 'Iason Jordan', 'David Morgan', 'Brain John', 'Jack Swift']
customerPins = ['0123', '2575', '7275', '2312', '5049']
customerBalances = [10000, 20000, 20000, 40000, 10000]
deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 5
i = 0

# This statement below helps the program to run continuously.
while True:
    print("=====================================")
    print(" ----Welcome to Times Bank----       ")
    print("*************************************")
    print("=<< 1. Open a new account         >>=")
    print("=<< 2. Withdraw Money             >>=")
    print("=<< 3. Deposit Money              >>=")
    print("=<< 4. Check Customers & Balance  >>=")
    print("=<< 5. Exit/Quit                  >>=")
    print("*************************************")

    choiceNumber = input("Select your choice number from the above menu : ")

    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        try:
            NOC = int(input("Number of Customers : "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        i = i + NOC

        if i > 5:
            print("\nCustomer registration limit reached or too low.")
            i = i - NOC
        else:
            while counter_1 <= i:
                name = input("Input Fullname : ")
                customerNames.append(name)
                pin = input("Please input a pin of your choice : ")
                customerPins.append(pin)
                balance = 0
                try:
                    deposition = int(input("Please input an amount to deposit to start an account: "))
                    if deposition <= 0:
                        print("Deposit must be a positive value!")
                        customerNames.pop()
                        customerPins.pop()
                        continue
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    customerNames.pop()
                    customerPins.pop()
                    continue

                balance += deposition
                customerBalances.append(balance)

                print(f"\nName = {customerNames[counter_2]}")
                print(f"Pin = {customerPins[counter_2]}")
                print(f"Balance = {customerBalances[counter_2]} -/Rs")
                counter_1 += 1
                counter_2 += 1
                print("\n----New account created successfully!----")
                print("========================================")
            mainMenu = input("Press enter key to go back to main menu...")

    elif choiceNumber == "2":
        print("Choice number 2 is selected by the customer")
        name = input("Please input name: ")
        pin = input("Please input pin: ")
        if name in customerNames and pin in customerPins:
            index = customerNames.index(name)
            if customerPins[index] == pin:
                balance = customerBalances[index]
                print(f"Your Current Balance: {balance} -/Rs")

                try:
                    withdrawal = int(input("Input value to Withdraw: "))
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

                if withdrawal <= 0:
                    print("Withdrawal amount must be positive.")
                elif withdrawal > balance:
                    print("Insufficient balance!")
                else:
                    balance -= withdrawal
                    customerBalances[index] = balance
                    print("----Withdrawal Successful!----")
                    print(f"Your New Balance: {balance} -/Rs")
        else:
            print("Name and pin do not match!")
        mainMenu = input("Press enter key to go back to main menu...")

    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        name = input("Please input name: ")
        pin = input("Please input pin: ")
        if name in customerNames and pin in customerPins:
            index = customerNames.index(name)
            if customerPins[index] == pin:
                balance = customerBalances[index]
                print(f"Your Current Balance: {balance} -/Rs")

                try:
                    deposition = int(input("Enter the value you want to deposit: "))
                    if deposition <= 0:
                        print("Deposit must be a positive value.")
                        continue
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
                    continue

                balance += deposition
                customerBalances[index] = balance
                print("----Deposit Successful!----")
                print(f"Your New Balance: {balance} -/Rs")
        else:
            print("Name and pin do not match!")
        mainMenu = input("Press enter key to go back to main menu...")

    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        print("Customer name list and balances mentioned below:")
        for idx, name in enumerate(customerNames):
            print(f"-> Customer: {name}")
            print(f"-> Balance: {customerBalances[idx]} -/Rs")
        mainMenu = input("Press enter key to go back to main menu...")

    elif choiceNumber == "5":
        print("Thank you for using our banking system!")
        print("Goodbye!")
        break

    else:
        print("Invalid option selected! Please try again.")
        mainMenu = input("Press enter key to go back to main menu...")
