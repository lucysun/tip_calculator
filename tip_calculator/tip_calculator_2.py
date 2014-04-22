import sys

meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

tax_value = tax*meal
meal_with_tax = meal +tax_value
tip_value = tip*meal_with_tax
total = meal_with_tax + tip_value

print "The base cost of your meal: " '{:.2f}'.format(meal)
print "Tax: " '{:.2f}'.format(tax_value)
print "Tip: " '{:.2f}'.format(tip_value)
print "Total: " '{:.2f}'.format(total)