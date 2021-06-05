import random
action=input("What action would you like to perform, w=withdraw, d=deposit, c=check, e=change currency")
def withdrawal():
    pin=input("What is your pin number")
    currency=input("Whatt currency would you like to use")
    amount=input("how much money would you like to withdraw")
    print(amount, currency, "have been withdrew from", pin)

def deposit():
    pin=input("What is your pin number")
    currency=input("What currency would you like to use")
    amount=input("how much money would you like to deposit")
    print(amount, currency, "have been deposited to", pin)

def check():
    pin=input("What is your pin number")
    currency=input("What currency would you like to use")
    r=random.randint(10,10000)
    print(pin, "has", r, currency)

def exchange():
    pin=input("What is your pin number")
    currency=input("What currency are you currently using")
    currency2=input("What is the currency you would like to change to")
    change=int(input("what is the exchange rate of your first currency against your second"))
    r=random.randint(10,10000)
    c=r*change
    print("the", r, currency, "in", pin, "have been changed into", c, currency2)

if action=="w":
    withdrawal()

if action=="d":
    deposit()

if action=="c":
    check()

if action=="e":
    exchangee()