# Complete this ATM simulation
#balance = 1000
#pin = "1234"

#entered_pin = input("Enter PIN: ")
#if entered_pin == pin:
#    print("PIN accepted")
#    while True:
#        print("\n1. Check Balance")
#        print("2. Withdraw")
#        print("3. Deposit") 
#        print("4. Exit")
#        
#        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
balance = 1000
pin = 1234
entered_pin = int(input("Enter PIN: "))
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")  
        print("3. Deposit") 
        print("4. Exit")
        choice = int(input("Choose option: "))
        if choice == 1:
            print(f"Your Balance:{balance}"+" THB")
        elif choice == 2:
            Withdraw = float(input("How much do you want to Withdraw: "))
            if Withdraw <= balance:
                balance = balance - Withdraw
                print(f"Please collect your maney\nTotal balance: {balance}")
            else:
                print("Insufficient balance")
        elif choice == 3:
            amount = float(input("Deposit amount:"))
            if amount < 0:
                print("cann't Deposit less then 0")
            else:
                balance = balance + amount
                print(f"your balance now = {balance}")
        elif choice == 4:
            break
        else:
            print("error")
            continue
        
else:
    print("Invalid PIN")
