#first trick

arr =[54,78,9,13,45,81,59]
def insertion(arr):
    for i in range(1, len(arr)):
        currentvalue = arr[i]
        position = i
        while(position>0 and arr[position-1]>currentvalue):
            arr[position]=arr[position-1]
            position=position-1
            arr[position] = currentvalue
    print(arr)
insertion(arr)

# #second trick

# array = [1,3,4,5,2]   #0,1,2,3,4
# #here wil are shifting all numbers from right to left
# temp =array[4] #store 2 i temporary variable
# array[4] = array[3]
# array[3] = array[2]
# array[2] = array[1]
# array[1] = temp

#doing the same above in for loop for 1 iteration
#print(array)
# array =[1,3,4,5,2]
# index = len(array) -1
# key = array[index]
# j =index - 1
# while j >= 0 and key < array[j]:
#     print(j)
#     array[j+1] = array[j]
#     j -= 1
# array[j + 1] = key
# print(array)

# Traverse through 1 to len(arr)
# arr = [12,11,13,5,6]
# arr =[11,12,13,5,6] #First class
# arr = [11,12,13,5,6] #Second clas
# arr = [5,11,12,13,6] #third class
# arr = [5,6,11,12,13] #forth class
#
# 1 to 4
# for i in range(1, len(arr)):
#     #i =4
#     key =arr[i] #6
#     #move elements of arr[0..i-1],that are
#     #greater than key,toone position ahead
#     #of their current position
#     j=i-1
#     while j>=0 and key < arr[j]:
#         arr[j+1] = arr[j]
#         j -=1
#         arr[j+1] = key
# print(arr)



