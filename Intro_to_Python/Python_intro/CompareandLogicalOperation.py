'''
Created on 2021/09/23

@author: Tho Nguyen
'''
#x = 5==4
#print(x)
degree = input("What is your degree? ")

if degree == "Master" or degree == "master" or degree =="PhD" or degree == "phd":
    experYear = input("How many year of  exprience do you have: ")
    if int(experYear) <=2:
        print("Sorry! You dont have enought exp")
    else:   
        print("Yeah, you can get master degree")
else:
    print("You dont have the required degree!")