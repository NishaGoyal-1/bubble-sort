arr= [1,2,3,4,5]
n = len(arr)
# Pick Starting Point
for i in range(0, n):
        # Pick Ending Point
    for j in range(i, n):
        # Print Subarray between starting and ending
        for k in range(i, j+1):
            print(arr[k], end=" ")
        print(" ", end=" ")


# start = 0
# while start < len(arr):
#     end = start
#     while end < len(arr):
#         print(arr[start:end + 1])
#         end +=1
#     start +=1


# sub_array = []
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         sub_array.append(arr[j])
# print(sub_array)



