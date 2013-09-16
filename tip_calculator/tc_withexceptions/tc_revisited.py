import sys
import tc_functions


# try: 
meal = sys.argv[1]
tax = sys.argv[2]
tip_percent = sys.argv[3]

print meal
print tax
print tip_percent

# except ValueError:
# 	print("Sorry, you must supply numbers for all input parameters to this script. Try again")
# 	meal = raw_input("Enter meal cost: ")
# 	tax = raw_input("Enter tax rate: ")
# 	tip_percent = raw_input("Enter tip rate: ")

meal_info = tc_functions.calculate_meal_costs(meal, tax, tip_percent)


