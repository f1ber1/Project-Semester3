import random

number = random.randint(10,20)
res = int(input("please guess a number:"))

while(True):
	if(res == number):
		print("Congratulation")
		break;
	res = int(input("Sorry,the answer is not correct,please guess again:"))
