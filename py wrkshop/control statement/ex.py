from selectors import SelectSelector

balance=10000
amount=int(input("enter amount :"))
if(amount>balance):
    print ("balance edhe")
else:
    print ("your amount has debited")
    balance-=amount
    print (f"your new amount {balance}")
