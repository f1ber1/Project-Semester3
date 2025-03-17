age = int(input("please enter your age:"))
if(age <= 19):
	print("you have student discounts")
elif(age >= 20 and age <= 54):
	print("you have no age discounts")
else:
	print("you can receive senior discounts")
