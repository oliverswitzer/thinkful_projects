import sys
import tc_functions


def main():
	try: 
		meal = float(sys.argv[1])
		tax = float(sys.argv[2])
		tip_percent = float(sys.argv[3])

	except ValueError:
		print("Sorry, you must supply numbers for all input parameters to this script. Try again")
		meal = raw_input("Enter meal cost: ")
		tax = raw_input("Enter tax rate: ")
		tip_percent = raw_input("Enter tip rate: ")

	meal_info = tc_functions.calculate_meal_costs(float(meal), float(tax), float(tip_percent))

	print "***" * 25
	print "The cost of your meal plus tax is {:.2f} ".format(meal_info["meal_with_tax"]) 
	print "With a {0} tip rate, you should leave ${1} for tip".format(meal_info["tip_rate"], meal_info["tip_value"])

 
if __name__ == '__main__':
    main()