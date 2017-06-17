# By Sam the Great from forums
# That freaking superhero has been frequenting Udacity
# as his favorite boss battle fight stage. The 'Udacity'
# banner keeps breaking, and money is being wasted on
# repairs. This time, we need you to proceduralize the
# fixing process by building a machine to automatically
# search through debris and return the 'Udacity' banner
# to the company, and be able to similarly fix other goods.

# Write a Python procedure fix_machine to take 2 string inputs
# and returns the 2nd input string as the output if all of its
# characters can be found in the 1st input string and "Give me
# something that's not useless next time." if it's impossible.
# Letters that are present in the 1st input string may be used
# as many times as necessary to create the 2nd string (you
# don't need to keep track of repeat usage).

# NOTE: # If you are experiencing difficulties taking
        # this problem seriously, please refer back to
        # "Superhero flyby", the prequel, in Problem Set 11.

# TOOLS: # if statement
         # while loop
         # string operations
         # Unit 1 Basics

# BONUS: # 
# 5***** #  If you've graduated from CS101,
#  Gold  #  try solving this in one line.
# Stars! #

def fix_machine(debris, product):
    ### WRITE YOUR CODE HERE ###
    n = 0
    while n < len(product):
        if debris.find(product[n]) == -1:
            return "Give me something that's not useless next time."
        n += 1
    return product

### TEST CASES ###
print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'





# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def isLeapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True
        
def yearToDate(year, month, day):
    daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeapYear(year):
        daysOfMonths[1] = 29
    m = 1
    while m < month:
        day = day + daysOfMonths[m-1]
        m += 1
    return day
    
def daysBetweenYears(year1, year2):
    days = 0
    while year1 < year2:
        days += 365
        if isLeapYear(year1):
            days += 1
        year1 += 1
    return days

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # print "SEE ANSWER", daysBetweenYears(year1, year2), yearToDate(year1, month1, day1), yearToDate(year2, month2, day2)
    return daysBetweenYears(year1, year2) - yearToDate(year1, month1, day1) + yearToDate(year2, month2, day2)

# Test routine

def test():
    test_cases = [((2012,6,29,2012,6,30),1),
                  ((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed" #result
        else:
            print "Test case passed!"

test()





#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    blank = '   '
    abacus = '|00000*****|'
    i = 1000000000
    while i > 0:
        index = value / i
        print abacus[:-index-1] + blank + abacus[-index-1:]
        value = value - index * i
        i = i / 10

###  TEST CASES
print "Abacus showing 0:"
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print "Abacus showing 12345678:"
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print "Abacus showing 1337:"
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|





# By Ashwath from forums

# A leap year baby is a baby born on Feb 29, which occurs only on a leap year.

# Define a procedure is_leap_baby that takes 3 inputs: day, month and year
# and returns True if the date is a leap day (Feb 29 in a valid leap year)
# and False otherwise.

# A year that is a multiple of 4 is a leap year unless the year is
# divisible by 100 but not a multiple of 400 (so, 1900 is not a leap
# year but 2000 and 2004 are).

def isLeapYear(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    else:
        return True

def is_leap_baby(day,month,year):
    # Write your code after this line.
    if day == 29:
        if month == 2:
            if isLeapYear(year):
                return True
    return False

# The function 'output' prints one of two statements based on whether 
# the is_leap_baby function returned True or False.

def output(status,name):
    if status:
        print "%s is one of an extremely rare species. He is a leap year baby!" % name
    else:
        print "There's nothing special about %s's birthday. He is not a leap year baby!" % name

# Test Cases

output(is_leap_baby(29, 2, 1996), 'Calvin')
#>>>Calvin is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(19, 6, 1978), 'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29, 2, 2000), 'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28, 2, 1976), 'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!
