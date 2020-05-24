# to find the profit earned in any product

cp = float(input("Enter the cost price of the product :"))
sp = float(input("Enter the selling price of the product :"))
profit = sp - cp
ui = int(input("Enter the amount of profit u want to increase : "))
ud = float(1 + (ui/100) )
new_sp = ud * profit + cp
print("The profit earned is : ", profit)
print("To increase in the profit by", ui ,"% the sellimg price should be" , new_sp)
