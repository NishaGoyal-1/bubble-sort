arr = [-2,1,-3,4,-1,2,1,-5,4]
sub_arr = []
for i in range (len(arr)):
    #sub_arr = []
    for j in range(i, len(arr)):
        sub_arr.append(arr[j])
        sum = 0
        for k in range(len(sub_arr)):
            sum = sum + sub_arr[k]
        sub_arr.append(sum)
print(max(sub_arr))