#fibonacci series
# 0,1,1,2,3,5,8,13,21,34,55,89

#n =int(input("enter a no.:"))
n = 100
a = 0
b = 1
c = a + b
while c <= n:
    print(c)
    a = b
    b = c
    c = a + b


# def fibonacci(n):
#     a =0
#     b =1
#     if n < 0:
#         print("incorrect input")
#     elif n==0:
#         return a
#     elif n==1:
#         return b
#     else:
#         for i in range(2,n+1):
#             c = a+b
#             a = b
#             b = c
#         return b
# print(fibonacci(10))