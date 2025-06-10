class BankAccount:
    def __init__(self):
        self.balance = 0.0
        print('Bank account Initiated\n')
        service = True
        while(service):

            self.option = input(f'''
Welcome to Bank

1. Check Balance
2. Withdraw 
3. Deposit
0. Exit
                    
=> ''')
            if self.option == '1':
                self.show_balance()
                continue

            elif self.option == '2':
                self.withdraw()
                continue

            elif self.option == '3':
                self.deposit()
                continue
            elif self.option == '0':
                print('Thank You, Visit again')
                exit()
                break
            else:
                print('Invalid Input, try again...')
                continue
        
    
    def show_balance(self) -> float:
        print(f"Current Balance  {self.balance}")

    def withdraw(self):
        amount = input('Enter withdraw amount : ')
        try:
            amount = float(amount)
            if amount <= 0 or self.balance < amount:
                print('Invalid amount')

            else:
                self.balance -= amount
                print("Please collect your cash :\n💰💰💰")
                self.show_balance()

        except Exception as e:
            print('Invalid amount...')
        finally:
            return
        
    def deposit(self):
        amount = input('Enter deposit amount : ')
        try:
            amount = float(amount)
            if amount >0:
                self.balance += amount
                print(f"{amount} credited to you account 💰💰💰")
                self.show_balance()

            else:
                print('Invalid amount')

        except Exception as e:
            print('Invalid amount...')
        finally:
            return
    



if __name__ == '__main__':
    bank = BankAccount()

