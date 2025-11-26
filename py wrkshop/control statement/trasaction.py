balance=10000
type=input("credit/debit:")
if type=="credit":
    amount = int(input("enter your amount :"))
    balance+=amount
    print(f"your new amount {balance}")
elif(type=="debit"):
    amount = int(input("enter your amount :"))
    balance-=amount
    print(f"your new amount {balance}")