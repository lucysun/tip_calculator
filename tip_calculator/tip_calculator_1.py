meal = float(raw_input("Enter the base cost of the meal: "))
tax = float(raw_input("Enter the tax rate as a decimal: "))
tip = float(raw_input("Enter the tip rate as a decimal: "))

tax_value = tax*meal
meal_with_tax = meal +tax_value
tip_value = tip*meal_with_tax
total = meal_with_tax + tip_value

print "The base cost of your meal: " '{:.2f}'.format(meal)
print "Tax: " '{:.2f}'.format(tax_value)
print "Tip: " '{:.2f}'.format(tip_value)
print "Total: " '{:.2f}'.format(total)