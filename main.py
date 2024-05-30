def calculate_discount(price,discount_percent):
    if(discount_percent>20):
        return price*discount_percent/100
    else:
        return price
x= calculate_discount(200,90)
y = calculate_discount(200,10)
print(x,y)