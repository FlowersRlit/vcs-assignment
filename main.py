### dummy file

### main data
userBalance = 50000
currency = "Rp"

### shop logic
banana = 10000
melon = 7000
apple = 16000
purchaseConfirm = "Are you sure you want to buy this item? (y/n)"
purchaseSuccess = "Thank you for buying"
cancel = "Transaction cancelled. Exiting..."
otherInput = "Wrong input!"
afterTransaction = "Your balance: "

print("Current available items on the store:\na. Banana - " + currency + str(banana) + "\nb. Melon - " + currency +str(melon) + "\nc. Apple - " + currency + str(apple))
userInput = input("What would you like to buy? ").lower()

### transaction logic
if userInput == "a" or "banana":
    print(purchaseConfirm)
    userConfirm = input(">>> ").lower()
    if userConfirm == "y":
        userBalance -= banana
        print(afterTransaction + currency + str(userBalance))
    elif userConfirm == "n":
        print(cancel)
    else:
        print(otherInput)
elif userInput == "b" or "melon":
    print(purchaseConfirm)
    userConfirm = input(">>> ").lower()
    if userConfirm == "y":
        print(purchaseSuccess)
        userBalance -= melon
        print(afterTransaction + currency + str(userBalance))
    elif userConfirm == "n":
        print(cancel)
    else:
        print(otherInput)
elif userInput == "c" or "apple":
    print(purchaseConfirm)
    userConfirm = input(">>> ").lower()
    if userConfirm == "y":
        print(purchaseSuccess)
        userBalance -= apple
        print(afterTransaction + currency + str(userBalance))
    elif userConfirm == "n":
        print(cancel)
    else:
        print(otherInput)
else:
    print(cancel)
