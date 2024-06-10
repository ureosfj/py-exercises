# Write a Python program to calculate the difference between 
# a given number and 17. If the number is greater than 17, return twice the absolute difference.

golden = 17
num = int(input('send number '))
if num > golden:
    res = (num-golden)*2
    
else:
    res = golden-num
    
print(res)