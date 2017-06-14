# Write Python code that prints out the number of hours in 7 weeks.
print 24 * 7 * 7

# Write Python code that stores the distance 
# in meters that light travels in one 
# nanosecond in the variable, nanodistance. 
# These variables are defined for you:
speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion
# After your code, running the following:
# print nanodistance
# should output: 0.2998
# Note that nanodistance must be a decimal number.
# ASSIGN nanodistance BELOW this line
nanodistance = speed_of_light / nano_per_sec
print nanodistance

# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
print s[:2] + t[3:]

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.
text = "first hoo" 
# ENTER CODE BELOW HERE
print text.find('hoo')

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.
# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string
# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1
text = "all zip files are zipped" 
# ENTER CODE BELOW HERE

# IMPORTANT BEFORE SUBMITTING: 
# You should only have one print command in your function
