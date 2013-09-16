

meal = raw_input("What was the base price of your meal? $")
tax = raw_input("What is the tax rate (percentage) in your state? %")
tip = raw_input("What percentage of your meal would you like to tip? %")

tax_dec = float(tax)/100.0 #make the tip/tax a decimal number
tip_dec = float(tip)/100.0

tax_value = float(meal)*tax_dec #getting the tax value of the meal
meal_with_tax = float(meal) + tax_value #adding the tax value of the meal to the base meal price
tip_value = meal_with_tax*tip_dec #getting raw tip value of the meal

total = meal_with_tax + tip_value #the total amount including tip

print "The base cost of your meal is ${:.2f} ".format(float(meal))
print "The tax value of your meal is ${:.2f} ".format(tax_value)
print "With a {:.0f}% tip rate, you owe ${:.2f} in tip ".format(float(tip), tip_value)
print "The grand total is ${:.2f} ".format(total)