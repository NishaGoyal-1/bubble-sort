import sys
arr= [-2,-3,4,-1,-2,1,5,-3]
max_sum = -sys.maxsize -1
print(max_sum)
curr_sum = 0
start = 0
end = 0
for i in range(len(arr)):
    curr_sum= curr_sum + arr[i]
    #print(curr_sum)
    if curr_sum > max_sum:
        max_sum = curr_sum
        end = i
    if curr_sum < 0:
        curr_sum = 0
        start = i+1
print(start)
print(end)
sub = arr[start:end+1]
print(sub)
print(max_sum)

