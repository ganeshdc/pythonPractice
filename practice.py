#take input from user
name = str(input("Enter your name:"))
age = int(input("Enter your age:"))
print(name,'your age is',age)

#IF STATEMENT
if (age > 30):
	print('You are mature enought now.')
else:
	print('You are still young.')

#TERNARY OPERATOR
output = "You are mature enought now." if(age > 30) else "You are still young."
print('Ternary Operator output:',output)



#LIST
thislist = ['one', 'two', 'three', 'four']
print(type(thislist))
for x in thislist:
	print(x)

for i in range(len(thislist)):
  print(i,thislist[i])
