def userinput():
    first_input = int(input("enter your first number: "))
    second_input = int(input("enter your second number: "))
    return first_input, second_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def mul(a=0,b=0):
    return a*b

print("welcome to calculator")
while True:
    print("select the choose :\n 1: add \n 2: sub \n 3: mul \n 4: quit")
    choose=int(input("enter your choice: "))

    if(choose==1):
        x,y=userinput()
        print(f"addtion of two number: {add(x,y)}")

    elif(choose==2):
        x,y=userinput()
        print(f"subtraction of two number: {sub(x,y)}")

    elif(choose==3):
        x,y=userinput()
        print(f"multiplication of two number: {mul(x,y)}")

    elif(choose==4):
        print("yen macchi arama")
        break



