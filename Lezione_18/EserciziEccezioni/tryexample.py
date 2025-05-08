class BankAccount:
    def __init__(self, initial_balance: float):
        # Assert that the initial balance is a non-negative value
        assert initial_balance >= 0, "Initial balance cannot be negative."
        self.balance = initial_balance
    
    def deposit(self, amount: float):
        # Assert that the deposit amount is positive
        assert amount > 0, "Deposit amount must be positive."
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")
    
    def withdraw(self, amount: float):
        # Assert that withdrawal amount is positive
        assert amount > 0, "Withdrawal amount must be positive."
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew ${amount}. New balance is ${self.balance}.")
    
    def get_balance(self):
        return self.balance

def simulate_bank_operations():
    account = None
    try:
        # Simulating user input for account creation and operations
        initial_balance = float(input("Enter initial balance for the account: $"))
        # Assert to ensure that the balance is valid
        assert initial_balance >= 0, "Initial balance must be a positive number or zero."
        account = BankAccount(initial_balance)
        
        # Perform operations: deposit and withdraw
        while True:
            print("\nChoose an operation:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check balance")
            print("4. Exit")
            choice = input("Enter choice (1-4): ")
            
            if choice == '1':
                try:
                    deposit_amount = float(input("Enter deposit amount: $"))
                    assert deposit_amount > 0, "Deposit amount must be positive."
                    account.deposit(deposit_amount)
                except ValueError as e:
                    print(f"Error: {e}")
                except AssertionError as e:
                    print(f"Error: {e}")
            elif choice == '2':
                try:
                    withdraw_amount = float(input("Enter withdrawal amount: $"))
                    account.withdraw(withdraw_amount)
                except ValueError as e:
                    print(f"Error: {e}")
                except AssertionError as e:
                    print(f"Error: {e}")
            elif choice == '3':
                print(f"Current balance: ${account.get_balance()}")
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except ValueError as e:
        print(f"Input error: {e}")
    except AssertionError as e:
        print(f"Assertion error: {e}")
    else:
        print("Bank operations completed successfully.")
    finally:
        if account:
            print(f"\nFinal account balance: ${account.get_balance()}")
        print("Thank you for using the Bank system.")

simulate_bank_operations()