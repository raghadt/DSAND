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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""





codes_list = []
count_080 = 0

# for record in calls:
#   if record[0] starts with (080):
#     if record[1] starts with '(' then add what is between '(' and ')' to the container. 
#     if record[1] starts with '140' then add '140' to the container.
#     if record[1] starts with 7, 8, or 9 then add the first four digits of record[1] to the container.

for i in range(len(calls)):
  code_val = ''
  caller = calls[i][0]
  rec = calls[i][1]

  if caller[:5] == '(080)':
    if rec[0]=='(':
      paranthesis_index = rec.find(')')
      codes_list.append(rec[:paranthesis_index+1])
    elif rec[:3] == '140':
      codes_list.append('140')
    else:
      codes_list.append(rec[:4])

count_080 = codes_list.count('(080)')

codes_set=sorted(set(codes_list))


print("The numbers called by people in Bangalore have codes:")
for i in list(codes_set):
  print(i)



"""

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
percent_080 = count_080/len(codes_list)*100
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent_080, 2)))