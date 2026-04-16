class Account:
    def __init__(self, title: str, balance: int):
        self.title = title
        self._balance = balance
    
    def get_balance(self) -> int:
        return self._balance

    # def _display_balance(self) -> None:
    #     pass

    def display_balance(self) -> None:
        balance = self.get_balance()
        print(f"Balance: ${balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
