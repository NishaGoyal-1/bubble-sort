l1 = ["mango", "grape"]
for i in l1:
    print(i)

#nested for loop
color = ["blue", "green", "yellow"]
item = ["book", "ball", "chair"]
for i in color:
    for j in item:
        print(i,j)

#while loop
i=0
while i<=10:
    print(i)
    i=i+1

i=1
n=2
while i<=10:
    print(n, "*", i, "=", n*i)
    i=i+1

#while with list
l1=[1,2,3,4,5]
i=0
while i<len(l1):
    l1[i]=l1[i]+100
    i=i+1
    print(l1)