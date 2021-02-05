"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers_set = set([calls[i][0] for i in range(len(calls))])

rec_set = set([calls[i][1] for i in range(len(calls))])

text_out_set = set([texts[i][0] for i in range(len(texts))])

text_in_set = set([texts[i][1] for i in range(len(texts))])

callers_set = callers_set - rec_set
callers_set = callers_set - text_out_set
callers_set = callers_set - text_in_set

callers_set= sorted(callers_set)

print("These numbers could be telemarketers: ")
for i in list(callers_set):
    print(i)