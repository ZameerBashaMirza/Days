

# name=input("Hey, what's your name: ")
# sales=float(input("Hey, what is the total sales for this month: "))
# commission=sales*13/100
# print(f"{name}! Your total sales are {sales} and this month you won the commission on sales is ${round(commission,2)}")

name=input("Please, tell me your name: ")
sales=input("Please, input your total month sales: ")
sales=int(sales)
commission=sales*13/100
commission=round(commission,2)
print(f"Hello {name}, your commissions this month are ${commission}")