### dummy file

### main data
userBalance = 50000
currency = "Rp"

### shop logic
Banana = 20000
Melon = 41000
Apple = 13000
purchaseConfirm = "Are you sure you want to buy this item? (y/n)"
purchaseSuccess = "Thank you for buying"
cancel = "Transaction cancelled. Exiting..."
otherInput = "Wrong input!"

print("Current available items on the store:\na. Banana - " + currency + str(Banana) + "\nb. Melon - " + currency +str(Melon) + "\nc. Apple - " + currency + str(Apple))
print("What would you like to buy?")

userInput = input(">>> ").lower()

### transaction logic
if userInput == "a" or "banana":
    print(purchaseConfirm)
    userConfirm = input(">>> ").lower()
    if userConfirm == "y":
        print(purchaseSuccess)
    elif userConfirm == "n":
        print(cancel)
    else:
        print(otherInput)
elif userInput == "b" or "melon":
    print(purchaseConfirm)
    userConfirm = input(">>> ").lower()
    if userConfirm == "y":
        print(purchaseSuccess)
    elif userConfirm == "n":
        print(cancel)
    else:
        print(otherInput)
elif userInput == "c" or "apple":
    print(purchaseConfirm)
    userConfirm = input(">>> ").lower()
    if userConfirm == "y":
        print(purchaseSuccess)
    elif userConfirm == "n":
        print(cancel)
    else:
        print(otherInput)
else:
    print(cancel)