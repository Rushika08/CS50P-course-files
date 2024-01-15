amount = 50
due = amount

while 0<amount<=50:
    print("Amount Due: ", amount, sep="")
    user_input = int(input("Insert Coin: "))
    if user_input==25 or user_input==10 or user_input==5:
        amount = amount-user_input
        due = amount
    else:
        continue

print("Change Owed: ", (-due), sep="")



