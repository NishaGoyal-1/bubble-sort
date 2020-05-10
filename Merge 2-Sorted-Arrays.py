#Agenda: merge 2 sorted arrays
#merge sort
#Revise
#O(n log(n))
#n*n

#n = 1024
#1024*1024
#1024*log(1024) = 1024 * 10

#mylist = [54,26,93,17,77,31,44,55,20]
def mergeSort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]

        #recursive  call on each half
        mergeSort(left)
        mergeSort(right)

        #merge 2 sorted array
        #Two iterators for traversing the two halves
        i = 0
        j = 0

        #Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                #the value from the left half has been used
                mylist[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                mylist[k] = right[j]
                j += 1
                # Move to the next slot
                k += 1
            #For all the remaining values
            while i < len(left):
                mylist[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                mylist[k] = right[j]
                j += 1
                k += 1
mylist = [54,26,90,17,77,31,44,55,20]
mergeSort(mylist)
print(mylist)