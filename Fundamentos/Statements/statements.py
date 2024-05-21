#<<---Statements--->>#
price = 20
budget = int(input("How many dollars you have? -> "))

if budget >= price: #-> Can buy the product
    print("I buy the product")
elif budget <= price - price / 4: #-> Need a little bit more of money to buy it
    print("I buy a discount of the product")
else: #-> Can't buy the product, I don't have enought money
    print("I don't buy it")    
    
"""
“If”, Checks if the statements are performed.
“Elif”, If the previous statement wasn't performed, it tries with this one.
“Else”, If none of the statements are performed we have the final option.
"""