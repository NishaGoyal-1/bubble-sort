# initializing number
num = 12321
rev =0
x = num
while num >0:
    rev = (rev*10) + num%10
    num =num//10

#for checking number is palindrome or not
if x==rev:
    print("number is palindrome")
else:
    print("number is not palindrome")


