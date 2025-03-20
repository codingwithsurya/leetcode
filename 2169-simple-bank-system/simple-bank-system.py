class Bank:

    def __init__(self, balance: List[int]):
        self.account_to_balance = {}
        self.n = len(balance)
        for account, bal in enumerate(balance):
            self.account_to_balance[account + 1] = bal 
        
    def is_valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid(account1) or not self.is_valid(account2) or self.account_to_balance[account1] < money:
            return False 
        
        self.account_to_balance[account1] -= money 
        self.account_to_balance[account2] += money
        return True 
        
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid(account):
            return False 
        
        self.account_to_balance[account] += money 
        return True 
        
    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid(account) or self.account_to_balance[account] < money:
            return False 
        
        self.account_to_balance[account] -= money 
        return True 

        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)