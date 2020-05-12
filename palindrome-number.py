# initializing number
num = 12321
reverse =0
x = num
while num >0:
    reverse = (reverse*10) + num%10
    num =num//10

#for checking number is palindrome or not
if x==reverse:
    print("number is palindrome")
else:
    print("number is not palindrome")

