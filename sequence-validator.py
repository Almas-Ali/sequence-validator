'''
Written by Md. Almas Ali @ 29 April, 2024

Validating 1/998_001 result 
'''

import decimal

base = 1
num = 998001

# get the full length output of the division to validate the result infinty
decimal.getcontext().prec = 3000-8 # 3000-8 to get the full length of the division
output = decimal.Decimal(base) / decimal.Decimal(num)
print(output) # printing raw decimals

# split the number by 3 digits and add a comma to separate them
output = str(output).split('.')[1] # remove the decimal point
output = [output[i:i+3] for i in range(0, len(output), 3)] # split the number by 3 digits

# for testing the values
assert len(output) == 999, 'The length of the output is not 999'

# loop testing all numbers
# for i in range(1000):
#     # AssertionError: The number is not correct at index: 998 value: 999
#     assert int(output[i]) == i, 'The number is not correct at index: ' + str(i) + ' value: ' + str(output[i])

# for display purpose
# output = ','.join(output) # add a comma to separate them
# print(output)

# write the output in a file
# with open('output.txt', 'w') as file:
#     # file.write(str(output))
#     for i in range(1000):
#         file.write(str(i) + ' -> ' + output[i] + '\n')

