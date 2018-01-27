#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

print "Print all the divisors of a number."
print "A divisor is a number that divides evenly into another number."
print "For example, 13 is a divisor of 26 because 26 / 13 has no remainder."
inp = int(raw_input("Enter a Number"))

series = range(1,inp+1)
divisorList = []
#print list
for i in series:
    if (inp % i == 0):
        divisorList.append(i)
print "the following numbers are divisors of "+str(inp)
for i in divisorList:
    print i
    