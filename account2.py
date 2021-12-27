from matplotlib import pyplot as plt 
import pandas as pd 
import datetime

#create inheritance 
# # parent class Customer 
# with attributes: name, balance, currency
# with methods: deposit, withdraw, show_balance
# create child class BankAccount 
# with attributes: name, balance, currency

# parent class 


class Customer:
     
     
    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        
    #add to string method
    def __str__(self):
        return " {}'s  Customer  with Balance: {}'{} ".format(self.name, self.balance, self.currency)
        
        
        
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print("Balance is {}".format(self.balance))
        
# child class
class BankAccount (Customer):
    
    
    
    def __init__(self, name, balance,currency):
        super().__init__(name, balance,currency)
        
    def __str__(self):
        return " {}'s  BankAccount  with Balance: {}'{} ".format(self.name, self.balance, self.currency)
    
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def show_balance(self):
        print("Balance is {}".format(  self.balance))

    # add method that shows account info
    def show_account_info(self):
        print("Account info: {}".format(self))
    
    # create a method that creates new object of the class BankAccount
    # with the balance of the customer that equals to 0  
    def create_new_account(self):
        return BankAccount(self.name, 0, self.currency)

    
    # add object to the list
    def add_to_list(self,my_list ):
        my_list.append(self)        
    def find_account( self,my_list):
        max_balance = 0
        for i in my_list:
            if i.balance > max_balance:
                max_balance = i.balance
                
        print(max_balance)
        
     
     
        
# create Transaction class that inherits from Customer class
# with attributes: sender, receiver, amount
# write the story of transactions to the pandas dataframe
# add methods show_transaction_story
# add method add_to_csv
class Transaction:
    def __init__(self, sender, receiver, amount ,date):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.date = date
    #create a method that transfers amount from sender to receiver
    def  transfer(self, sender, receiver, amount ,  date , df):
       #if sender has enough money to transfer 
       # and if currency is  the same then u can transfer
       # then transfer the amount
        if (sender.balance - amount) >= 0: # should be >= 0
            if sender.currency == receiver.currency:
                sender.withdraw(amount)
                receiver.deposit(amount)
           
            
                df.loc[len(df)] = [sender.name, receiver.name, amount  , date.strftime("%d/%m/%Y")]   
                print("Transfered \n")
                print("{} sent {} to {}  ".format(sender.name, amount, receiver.name))
            else:
                print("Not enough money or mismatched currency")
        
          
        
        print("{}'s balance is {} ".format(receiver, receiver.balance))
        print("{}'s balance is {}\n ".format(sender, sender.balance))
        
    # create a method that shows the transaction story from the csv file           
    def show_transaction_story_df(self):
        df = pd.read_csv('transactions.csv')
        print(df)
    
  
        
    def add_to_csv(self,df):
        #df = pd.DataFrame(columns=['sender', 'receiver', 'amount', 'date'])
        #  convert df to csv
        df.to_csv('transactions.csv', index=False)
        print("Transaction added to csv file \n")
    
    #create a method that shows the transaction story from the csv file of given customer
    def show_transaction_story_df_customer(self, customer , df):
        #df = pd.read_csv('transactions.csv')
        print(df[df['sender'] == customer])
        print("\n")
    
    def show_graph_of_transaction_story_df_customer(self, customer , df):
        #plot transaction story
        X = df[df['sender'] == customer]['date']
        y = df[df['sender'] == customer]['amount']
        plt.plot(X,y)
        plt.savefig('transaction_story.png')
        
        print("\n")

       
       