#pip install pandas
import pandas as pd 


#create inheritance 
# # parent class Account 
# with attributes: name, balance, currency
# with methods: deposit, withdraw, show_balance
# create child class BankAccount 
# with attributes: name, balance, currency

# parent class 


class Account:
     
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        
    #add to string method
    def __str__(self):
        return " {}'s  Account  with Balance: {}'{} ".format(self.name, self.balance, self.currency)
        
        
        
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print("Balance is {}".format(self.balance))
        
# child class
class BankAccount(Account):
    def __init__(self, name, balance,currency):
        super().__init__(name, balance,currency)
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print("Balance is {}".format(  self.balance))
    
    # add method that shows account info
    def show_account_info(self):
        print("Account info: {}".format(self))
        
        
# create Transaction class that inherits from Account class
# with attributes: sender, receiver, amount
# write the story of transactions to the pandas dataframe
# add methods show_transaction_story
# add method add_to_csv
class Transaction:
    # add date field to the class 
    def __init__(self, sender, receiver, amount  ):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    
    
    #create a method that transfers amount from sender to receiver
    def  transfer(self, sender, receiver, amount , df):
       #if sender has enough money to transfer 
       # then transfer the amount
        if (sender.balance - amount) >= 0: # should be >= 0
           sender.withdraw(amount)
           receiver.deposit(amount)
           # add the transaction to the dataframe and then add to csv
           df.loc[len(df)] = [sender.name, receiver.name, amount ]   
           #self.add_to_csv(df)
           # write the transaction to the csv file
           
           
           print("{} sent {} to {}  ".format(sender.name, amount, receiver.name)) 
        else:
            print("Not enough money")
        
          
        
        print("{}'s balance is {} ".format(receiver, receiver.balance))
        print("{}'s balance is {}\n ".format(sender, sender.balance))
        
    # create a method that shows the transaction story from the csv file           
    def show_transaction_story_df(self):
        df = pd.read_csv('transactions.csv')
        print(df)
        
        
    def add_to_csv(self, df):
        df.to_csv('transactions.csv', index=False)
        print("Transaction added to csv file \n")
        

        
        
#create Account class 
acc1 = Account("John", 100, "USD")
acc2 = Account("Mary", 200, "USD")

# create a BankAccount object
Bacc1 = BankAccount("John", 100, "USD")
Bacc2 = BankAccount("Mary", 200, "USD")
# create a Transaction object
T1 = Transaction("John", "Mary", 100)

df = pd.DataFrame(columns=['sender', 'receiver', 'amount'])


# check methods
acc1.show_balance()
acc1.deposit(50)
acc1.show_balance()
acc1.withdraw(10)
acc1.show_balance()

Bacc1.show_account_info()
Bacc2.show_account_info()

T1.transfer(acc1, acc2, 10, df)
T1.transfer(acc2,acc1,25, df)
T1.transfer(acc1,acc2,30, df)
T1.transfer(acc2,acc1,15, df)
print("this line --------------------------------")
T1.add_to_csv(df)
T1.show_transaction_story_df()
