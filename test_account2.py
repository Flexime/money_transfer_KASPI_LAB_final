# add account2.py 
from account2 import Customer, BankAccount , Transaction

from matplotlib import pyplot as plt 
import pandas as pd 
import datetime
    
#create Customer object
cust1 = Customer("John", 100, "USD")
cust2 = Customer("Mary", 200, "USD")

# create a BankAccount object

acc1 = BankAccount("John", 100, "USD")
acc2 = BankAccount("Mary", 200, "USD")
acc3 = BankAccount("John", 200, "USD")
# create a Transaction object
trans1 = Transaction(cust1, cust2, 50, datetime.datetime.now())

# add to list 
my_list = []
acc1.add_to_list(my_list)
acc2.add_to_list(my_list)
print("Biggest balance is:")
acc2.find_account(my_list)

df = pd.DataFrame(columns=['sender', 'receiver', 'amount', 'date'])
trans1.add_to_csv(df)

# check methods
trans1.transfer(acc1, acc3,100, datetime.datetime.now() , df)
trans1.transfer(acc2, acc1,50, datetime.datetime.now() , df )
trans1.transfer(acc2, acc2,25,   datetime.datetime.now() + datetime.timedelta(days=1) , df )
print("Marrry story: ") 
trans1.show_transaction_story_df_customer("Mary" , df)
trans1.add_to_csv(df)

trans1.show_transaction_story_df()
trans1.show_graph_of_transaction_story_df_customer("Mary", df)