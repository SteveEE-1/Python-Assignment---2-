class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
        else:
            print("Not enough balance to withdraw")

    def disp_bal(self):
        return self.balance


def save_pin(pin):
    with open("pin1.txt", "w") as f:
        f.write(pin)


def load_pin():
    try:
        with open("pin1.txt", "r") as f:
            return f.read().strip()
    except:
        return None


def save_balance(balance):
    with open("balance1.txt", "w") as f:
        f.write(str(balance))


def load_balance():
    try:
        with open("balance1.txt", "r") as f:
            return float(f.read())
    except:
        return 1000.0


pin = load_pin()
if pin is None:
    while True:
        new_pin = input("Set a 4-digit PIN: ")
        if new_pin.isdigit() and len(new_pin) == 4:
            save_pin(new_pin)
            pin = new_pin
            print("PIN set!\n")
            break
        else:
            print("PIN must be 4 digits.")

for i in range(3):
    entered = input("Enter your PIN: ")
    if entered == pin:
        print("Login successful!\n")
        break
    else:
        print("Incorrect PIN.")
else:
    print("Too many attempts. Exiting.")
    exit()

balance = load_balance()
atm = ATM(balance)

while True:
    print("\n--- ATM MENU ---")
    print("1. View Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: {atm.disp_bal():.2f}")
    elif choice == "2":
        amt = input("Enter amount to deposit: ")
        atm.deposit(float(amt))
    elif choice == "3":
        amt = input("Enter amount to withdraw: ")
        atm.withdraw(float(amt))
    elif choice == "4":
        save_balance(atm.disp_bal())
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid option.")
