# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(s):
    words = s.split()
    return len(words)

passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)
#>>>56





# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(rtt_ms, dist_km):
    rtt_s = rtt_ms/1000.0
    speed = (2*dist_km)/rtt_s
    return speed/300000


print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?





# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(sec):
    hr = int(sec/3600)
    s = str(hr) + ' hour'
    if hr != 1:
        s = s + 's'
    
    min = int((sec - hr*3600)/60)
    s = s + ', ' + str(min) + ' minute'
    if min != 1:
        s = s + 's'
        
    sec = sec - hr*3600 - min*60
    s = s + ', ' + str(sec) + ' second'
    if sec != 1:
        s = s + 's'
    
    return s


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds





# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(sec):
    hr = int(sec/3600)
    s = str(hr) + ' hour'
    if hr != 1:
        s = s + 's'
    
    min = int((sec - hr*3600)/60)
    s = s + ', ' + str(min) + ' minute'
    if min != 1:
        s = s + 's'
        
    sec = sec - hr*3600 - min*60
    s = s + ', ' + str(sec) + ' second'
    if sec != 1:
        s = s + 's'
    
    return s

def download_time(filesize, size_unit, bandwidth, band_unit):
    sizes = [ ['kb', 2**10], ['kB', (2**10) * 8],
              ['Mb', 2**20], ['MB', (2**20) * 8],
              ['Gb', 2**30], ['GB', (2**30) * 8],
              ['Tb', 2**40], ['TB', (2**40) * 8] ]
    for unit in sizes:
        if size_unit == unit[0]:
            filesize = filesize * unit[1]
            #print 'filesize',filesize
        if band_unit == unit[0]:
            bandwidth = bandwidth * unit[1]
            #print 'bandwidth',bandwidth
            
    sec = (1.0*filesize) / bandwidth
    return convert_seconds(sec)


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
#0 hours, 37 minutes, 32.8 seconds
