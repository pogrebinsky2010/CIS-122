G'''valentines shopping cart list Talaba Pogrebinsky lab3d'''

product_list = ['cards', 'flowers', 'chocolates', 'heart boxes', 'neklace', 'braclet']
price_list = [2.95, 19.99, 10.99, 15.99, 100.00, 75.00]

cart_list =[]

def show_menu(products, prices):
    n = len(products)
    for i in range(n):
        print(i + 1, products[i], prices[i])
        
def get_price(option):
    if (option == 1):
        price = 2.95
        return round(price, 2)
    elif (option == 2):
        price = 19.99
        return round(price, 2)
    elif (option == 3):
        price = 10.99
        return round(price, 2)
    elif (option == 4):
        price = 15.99
        return round(price, 2)
    elif (option == 5):
        price = 100.00
        return round(price, 2)
    elif (option == 6):
        price = 75.00
        return round(price, 2)
   
        
totalPrice = float(0)
totalItems = 0.0
action = input('''Shop for valentine specials (y or n): ''')
while action == 'y':
    show_menu(product_list, price_list)
    choice = int(input("Please choose a product by selecting 1-6: "))
    print(choice)
    price = get_price(choice - 1)
    totalPrice += price
    totalItems += 1
    offset = choice - 1
    cart_list.append(offset)
    print(" you added", product_list[offset], 'to your cart for $', price_list[offset])
    action = input('''shop for more valentine specials ( y or no)  or you can type,
               'checkout' or 'cancel' to cancel your current order. ''')
    
    i = 0
    count = 1
while (action == 'checkout' and count <= totalItems):
       
       
        print("option ", cart_list[i], "was ", get_price(cart_list[i]) )
        i += 1
        count += 1
        
print("your total is: " , totalPrice )    
