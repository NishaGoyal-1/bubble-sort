# mylist = [14,51,11,12]
# mylist2 = []
# for i in (3,2,1,0):
#     mylist2.append(mylist[i])
# mylist = mylist2
# print(mylist)

#second trick
arr =[1,2,3,4,5]
def reverse_array(arr):
    mid = len(arr)//2
    start = 0
    while start < mid:
       arr[start],arr[len(arr)-1-start] = arr[len(arr)-1-start],arr[start]
       start +=1
    # for i in range(mid):
    #     arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
reverse_array(arr)
print(arr)

#copy reverse of array in other array
# def copy_reverse_array(arr):
#     destination_arr =[]
#     for i in reversed(range(len(arr))):
#         print(i)
#         destination_arr.append(arr[i])
#     print(destination_arr)
#     pass
# copy_reverse_array(arr)