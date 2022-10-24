def search_item(list, product):
    for i in range(len(list)):
        if list[i] == product:
            return True
    return False


grocery_list = ['avocado', 'milk', 'meat', 'chocolate','beverage']
product = 'fish'

command = input("What is your command?\n")
if command == 's':
    product = input("What are you looking for in the list?\n")
else:
    command = 'default'

if search_item(grocery_list, product):
    print("Product is Available!")
else:
    print("Product is not Available!")

print("Program ended.")
