
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import deque, defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# print(calls[0])
max_=-1
phone_number = ''

calls_dictionary= defaultdict(int)


for i in range(len(calls)):
    day_, month_, year_ = calls[i][2].split(' ')[0].split('-')
    # print(year_)
    if year_=='2016' and month_=='09':
        calls_dictionary[calls[i][0]] += int(calls[i][3])
        calls_dictionary[calls[i][1]] += int(calls[i][3])

# Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds

max_number, max_duration = max(calls_dictionary.items(), key=lambda x: x[1])

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_number,max_duration))
