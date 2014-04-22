from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", type="float", help="base cost of meal")
parser.add_option("-x", "--tax", dest="tax", type="float", help="tax in decimal form")
parser.add_option("-t", "--tip", dest="tip", type="float", help="tip in decimal form", default=0.2)

(options, args) = parser.parse_args()
if not options.meal:
    parser.error("dat meal cost wut")
if not options.tax:
    parser.error("bro do you even have a tax rate")

tax_value = options.meal * options.tax
meal_with_tax= tax_value + options.meal
tip_value = meal_with_tax * options.tip
total = meal_with_tax + tip_value


print "Base cost: {:.2f}".format(options.meal)
print "Tax: {:.2f}".format(tax_value)
print "Tip: {:.2f}".format(tip_value)
print "Grand Total: {:.2f}".format(total)