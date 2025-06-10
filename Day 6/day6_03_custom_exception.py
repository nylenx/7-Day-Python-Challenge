class NegativeDepositExeption(Exception):
    def __init__(self,amount,message='Entered a negative amount'):
        super().__init__(f'Deposit Failed when {message}; Entered amount {amount}')


if __name__ == '__main__':
    try:
        input_amount = float(input('Enter a deposit amount: '))

        if input_amount < 0 :
            raise NegativeDepositExeption(input_amount)
        else:
            print(f'💲💲💲 received, Balance: {input_amount} 💰💰💰')
    
    except NegativeDepositExeption as e:
        print(f'TRANSACTION DENIED: {e}')
    except ValueError:
        print("Please enter a numeric amount!!!")
    except TypeError as e:
        print(f'{e}')
