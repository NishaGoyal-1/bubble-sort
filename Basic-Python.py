a1='you are perfect'
print(a1[0])
print(a1[-1])
print(a1[0:7])
print(a1[:8])
print(len(a1))
print(a1.upper())
print(a1.lower())
print(a1.title())
print(a1.replace('y','m'))
print(a1.count("are"))

s1 = 'This is sparta!!!'
print(s1.find('sparta'))
print(s1.find('b'))

fruit = 'I like apples, mangoes, bananas'

print(fruit.split(','))

#Tuples in Python
tup1=(1,"a",True,2,"b",False)
print(tup1)
print(tup1[0])
print(tup1[1:4])

tup1 = (1,"a",True)
tup2 = (4,5,6)
print(tup1+tup2)

tup1 = ('sparta',300)
tup2 = (4,5,6)
print(tup1*3 + tup2)

#list in python
l1=[1,"a",2,"b",3,"c"]
l1.insert(1,"Sparta")
print(l1)
l1 = ["mango","banana","guava","apple"]
l1.sort()
print(l1)

#dictionary in python
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit["Mango"]=50
print(fruit)
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40,"Mango":50}
fruit["Apple"]=100
print(fruit)

fruit1={"Apple":10,"Orange":20}
fruit2={"Banana":30,"Guava":40}

fruit1.update(fruit2)
print(fruit1)

#set in python
s1={1,"a",True,2,"b",False}
s1.add("Hello")
print(s1)
s1.update([10,20,30])
print(s1)
s1.remove("b")
print(s1)
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}

print(s1.intersection(s2))

#Relational operator
a =10
b =20
print(a+b)
print(b%a)
print(a<b)
print(a>b)
print(a==b)
print(a!=b)

#logical operator
a=True
b=False
print(a&b)
print(b&a)
print(a&a)
print(b&b)
print(a|b)