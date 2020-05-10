arr = [14,33,27,10,35,19,42,44]

for i in range(len(arr)):
    index_min = 1
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[index_min]:
            index_min = j
    arr[i], arr[index_min] = arr[index_min], arr[i]
print(arr)

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


