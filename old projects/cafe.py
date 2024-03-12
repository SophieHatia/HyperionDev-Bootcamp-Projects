menu = ["croissant", "coffee", "sandwich", "tea"] #define list of items sold in a cafe
Total_Stock_Worth = 0

#define dictionary of stock amounts of each item
stock = {"croissant": 6, 
         "coffee": 30,
         "sandwich": 10,
         "tea": 25
        }

#define dictionary of price for each item
price = {"croissant": 3.50,
         "coffee": 2.80,
         "sandwich": 5.00,
         "tea": 2.00
        }

#iterate over the length of the list menu to find the value of each item
for i in range(len(menu)):
    print(menu[i], '\t', end= " ")
    stock_keys = stock.keys()
    price_keys = price.keys()
   # item_stock = stock_keys[]
    #item_price = price_keys[menu[i]]
    item_value = stock[menu[i]] * price[menu[i]]
    print(item_value)
    Total_Stock_Worth = Total_Stock_Worth + item_value #cumulatively add each item value together to find the total worth of stock
   
print("Total value of Stock Worth=", Total_Stock_Worth) #print the result
    
   
    





