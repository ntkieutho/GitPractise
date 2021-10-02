'''
Created on 2021/09/23

@author: Tho Nguyen
'''
#numA and numB
#subtract numB from numA
#print the result

numA = float(input("First: "))
numB = float(input("Second: "))
sub = numA-numB

print("Result: " + str(sub))

if sub<0:
    print("Negative num")
else:
    print("Positive num")