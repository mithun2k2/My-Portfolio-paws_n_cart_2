petFoodItems = []
shopping_cart = []
shopping_quant = []
total = 0
# Display the user menu and cart until chekout
# Add remove item using while loop
while True:
    print("\n")
    print("-"* 80)
    print("This is your shopping cart: ")
    print("-" * 80)
    print("Would you like to: ")
    print("1. Add an item to your cart: ")
    print("2. Remove an item from your cart: ")
    print("3.  Item purchase quantity: ")
    print("4. Checkout ")
    action = input("\nEnter the number of options you would like to choose: ")
    if action == "1":
        add = input("Want to add item to your cart? Y or N :")
        while add.lower() == "y":
            item = input("Enter your item to the list: ")
            print("{} has been added to your cart sucessfully.".format(item))
            petFoodItems.append(item)
            add = input("Want to add to your shopping list? Y or N: ")
        print()
        print("Here is your alphabetized shopping cart list")
        petFoodItems.sort()
        for item in petFoodItems:
                print(item)
    elif action == "2":
        # Find item that must be removed and check that it is in the cart
        remove = input("Which item would you like to remove: ")
        if remove in petFoodItems:
            # Remove items from cart
            index = petFoodItems.index(remove)
            petFoodItems.pop(index)
            print("{} has been removed from cart successfully".format(remove))
            print()
            print("Here is your alphabetized shopping cart list")
            for remove in petFoodItems:
                 print(remove)
        else:
            print(f"{remove} is not in your cart")
    elif action == "3":
        print('\nCHANGE ITEM QUANTITY', end='\n')
        name = str(input('Enter the item name: '))
        quant = int(input("How many units do you wish to purchase\n"))
        print()
        print("ITEM ", "QUANT", sep =" \t\t\t" )
        for name, quant in range(len(petFoodItems)):
            idx = petFoodItems.index(petFoodItems[name])
            
            idx = shopping_quant.index(shopping_quant[quant])
            print(petFoodItems[name], shopping_quant[quant], sep =" \t\t")

            
        else:   
            print('Item not found in cart. Nothing modified.')
    

