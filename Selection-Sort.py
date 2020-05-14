#A = [64, 25, 12, 22, 11]
A =[10,33,27,14,35,19,42,44]
# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

            # Swap the found minimum element with the first element
    A[i], A[min_idx] = A[min_idx], A[i]

print("Sorted array")
for i in range(len(A)):
    print("%d" % A[i])

# i = 0
#     index_min = 0
#     j=1, index_min = 0
#     j=2, index_min = 0
#     j=3, index_min = 0
#     j=4 to 7, index_min = 3
# arr = [10,33,27,14,35,19,42,44]
#
# i =1
#   j =2, index_min = 2
#   j =3, index_min = 3
#   j =4 to 7, index_min =3
# arr = [10,14,27,33,35,19,42,44]

