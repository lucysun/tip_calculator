import sys
from optparse import OptionParser
 
def calculate_rate(base, percentage):
    return base * percentage
 
def calculate_meal_costs(meal_base, tax_rate, tip_rate):
    """
    Calculates dollar amounts for tax, tip, and total meal cost
    """
    tax_value = calculate_rate(meal_base, tax_rate)
    meal_with_tax = tax_value + meal_base
    tip_value = calculate_rate(meal_with_tax, tip_rate)
    total = meal_with_tax + tip_value
    meal_info = dict(meal_base=meal_base,
                    tax_rate=tax_rate,
                    tip_value=tip_value,
                    tax_value=tax_value,
                    total = total)
    return meal_info
	
def enter_meal():
	while True:
		try:
			meal_base = float(sys.argv[1])
			break
		except ValueError:
			print "Please enter a number for the base cost of your meal." 
			meal_base = float(raw_input("Base cost of meal:"))
			break
	return meal_base

def enter_tax():
	while True:
		try:
			tax_rate = float(sys.argv[2])
			break
		except ValueError:
			print "Please enter the tax rate for the meal in decimal form."
			tax_rate = float(raw_input("Tax rate:"))
			break
	return tax_rate

def enter_tip():		
	while True:
		try:
			tip_rate = float(sys.argv[3])
			break
		except ValueError:
			print "Please enter the tip rate for the meal in decimal form."
			tip_rate = float(raw_input("Tip rate:"))
			break
	return tip_rate

def main():
	meal_base = enter_meal()
	tax_rate = enter_tax()
	tip_rate = enter_tip()
	meal_info = calculate_meal_costs(meal_base, tax_rate, tip_rate)
	print "The base cost of your meal is ${0:.2f}.".format(meal_info['meal_base'])
	print "The amount you should leave for tip is ${0:.2f}.".format(meal_info['tip_value'])
	print "Your total is ${0:.2f}.".format(meal_info['total'])

if __name__ == '__main__':
	main()
