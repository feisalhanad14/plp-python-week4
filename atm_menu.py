balance = 1000
correct_pin = "1234"

pin = input("Enter your 4-digit PIN: ")

# Check whether the PIN entered by the user is incorrect.
if pin != correct_pin:
    print("Incorrect PIN")

else:
    amount = int(input("Enter amount to withdraw: "))

    # Check whether the requested amount is within the available balance.
    if amount <= balance:
        balance = balance - amount
        print(f"Withdrawal successful.")
        print(f"New balance: {balance}")
    else:
        print("Insufficient funds")
