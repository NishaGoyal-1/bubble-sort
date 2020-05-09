#min element find in array
l1 = [3,4,5,1,2]
# n =len(l1)
# m = int("infinity")
# for i in range (0,n):
#     if l1[i] < m:
#         m = l1[i]
# print(m)

# l1.sort()
# print(l1[0])

#maximum element find in array
n = len(l1)
m = float("-infinity")
for i in range (0,n):
    if l1[i] > m:
        m = l1[i]
print(m)
