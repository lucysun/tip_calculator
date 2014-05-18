tip_calculator
==============
Three versions of a program that calculates restaurant tip and total bill value, based on input values of meal cost, tax rate, and tip rate:

1. raw_input.py accepts input through raw_input.

2. sysargv.py accepts input through sys.argv.

3. optparse.py accepts input through optparse OptionParser. The program sets a default tip rate of 20% and raises errors if a meal and tax rate are not specified.

4. exceptions.py accepts input through sys.argv. If the user inputs one or more strings at run time, the script intercepts the ValueError(s) and provides some informative feedback.
