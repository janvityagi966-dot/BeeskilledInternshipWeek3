class BankAccount:
    @staticmethod
    def get_amount(prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                else:
                    return amount
            except ValueError:
                print("Please enter a valid number.")


def main():
    pin = "1234"
    balance = 1000.00

    print("Welcome to the ATM")
    for attempt in range(3):
        if input("Enter your PIN: ") == pin:
            break
        print("Incorrect PIN.")
    else:
        print("Too many incorrect attempts. Your account is locked.")
        return

    while True:
        print("\n1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Your balance is: ${balance:.2f}")
        elif choice == "2":
            amount = BankAccount.get_amount("Enter deposit amount: $")
            balance += amount
            print(f"Deposit successful. New balance: ${balance:.2f}")
        elif choice == "3":
            amount = BankAccount.get_amount("Enter withdrawal amount: $")
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrawal successful. New balance: ${balance:.2f}")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()