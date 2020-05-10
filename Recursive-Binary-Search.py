#program for recursive binary search.return index of x in arr if present,else-1
def binary_search(arr,left,right,key):
    #check base case
    mid = left + (right - left)//2
    if right >= left:
        #if element is present at the middle itself
        if key == arr[mid]:
            return mid
        #if element is smaller than mid,then it can only be present in left subarray
        elif key < arr[mid]:
            return binary_search(arr,left,mid-1,key)
        #else the element can only be present in right subarray
        else:
            return binary_search(arr,mid+1,right,key)
    else:
        #element is not present in the array
        return -1

# #driver code
# arr =[2,3,4,10,40]
# x =11
#
# #function call
# result = binary_search(arr,0,len(arr)-1,x)
# if result !=-1:
#     print("element is present at index %d" % result)
# else:
#     print("element is not present in array")

arr = [10,14,19,27,33,35,42,44]
key =10
# left =0
# right =len(arr)-1

result = binary_search(arr,0,len(arr)-1,33)
print(result)

keys = [10,33,-1,-1100,1000,35]
for key in keys:
    result =binary_search(arr,0,len(arr)-1,key)
    print(result)

# left=0
# right=7
# mid=3, arr[mid] =27
# if key == arr[mid]:
#     return
# if key > arr[mid]:
# right side
# mid+1:right
#
# if key < arr[mid]
# left side
# left: mid-1
