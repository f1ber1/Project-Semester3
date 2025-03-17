num = int(input("please enter a number:"))

def factorial(num):
	res = 1
	i = 1
	while(i <= num):
		res = res * i
		i = i + 1
	print (res)
	
factorial(num)			
