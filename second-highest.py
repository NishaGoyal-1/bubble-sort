# def second_highest(arr):
#     if len(arr) < 2:
#         return "no element found"
#     if arr[0] > arr[1]:
#         first = arr[0]
#         second = arr[1]
#     else:
#         second = arr[0]
#         first = arr[1]
#
#     for i in range(2, len(arr)):
#         if arr[i] > first:
#             second = first
#             first =arr[i]
#         elif second < arr[i] < first:
#             second = first
#         else:
#             pass
#     return second
#
# arr = [12,30,10,72]
# #arr = [-1,-2,-3,-4]
# # arr = [2,2,2]
# # arr = [2]
# # arr = [-1,-2,-3,12]
# result = second_highest(arr)
# print(result)
# # elm < second
# elm > second and elm < first
# second = elm
# ele > first
# second = first
# first = ele

#nth highest value
a =[3,21,12,24,43,20]
def max(a):
    for i in range(0, len(a)-1):
        if a[i] > a[i + 1]:
            a[i],a[i+1] = a[i+1], a[i]
    return (a)
max(a)

def nth_highest_value(a):
    n =int(input("enter a number:"))
    if int(n) < len(a):
        for i in range(int(n)):
            max(a)
        print(a[len(a)-int(n)])

    else:
        print("provide input in range of array")

nth_highest_value(a)






