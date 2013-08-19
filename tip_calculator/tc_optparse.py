from optparse import OptionParser   #import the OptionParser object from this module
 
 
parser = OptionParser()

parser.add_option("-f", "--first", dest="first_arg", help="Please enter the cost of the meal")
parser.add_option("-s", "--second", dest="second_arg", help="Please enter the tax rate in your state",
                    default = 7.0)
                
(options, args) = parser.parse_args()

if !options.first_arg or !options.second_arg:
	parser.error("options -a and -b are mutually exclusive")

meal = options.first_arg 
tax = options.second_arg
tip = 7.5

tax_dec = float(tax)/100.0 	#make the tip/tax a decimal number
tip_dec = float(tip)/100.0

tax_value = float(meal)*tax_dec 	#getting the tax value of the meal
meal_with_tax = float(meal) + tax_value 	#adding the tax value of the meal to the base meal price
tip_value = meal_with_tax*tip_dec 	#getting raw tip value of the meal

total = meal_with_tax + tip_value 	#the total amount including tip

print "The base cost of your meal is ${:.2f} ".format(float(meal))
print "The tax value of your meal is ${:.2f} ".format(tax_value)
print "With a {:.1f}% tip rate, you owe ${:.2f} in tip ".format(float(tip), tip_value)
print "The grand total is ${:.2f} ".format(total)