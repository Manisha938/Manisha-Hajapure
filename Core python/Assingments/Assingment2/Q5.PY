#WAP to calculate selling price of book based on cost price and discount.
#take input from user
cost_price=float(input('enter cost price of book:'))
discount=float(input('enter discount percentage:'))

#formula
discount_amount=(cost_price*discount)/100
selling_price=cost_price-discount_amount

#result
print(f"The selling price of the book is: {selling_price}")
