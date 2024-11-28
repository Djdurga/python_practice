import array as arr

a = arr.array("i",[2,3,4,1,36,6,2,3,2])

for i in a:
    print(i, end=' ')
print()
print("First Element is : " , a[0])

a.append(5)
print("After append is : " , a[-1])

# SLICING
slic_arr = a[2:6]
print(slic_arr)
slic_arr = a[:]
print(slic_arr)

#COUNTING
count = a.count(2)
print("Count:", count)

#SEARCHING
s = a.index(2)
print("Index : ",s)

#Reversing
rev = a.reverse()
print("Reversed element: ",a)

#EXTEND
s = a.extend(5,63,2,7,8,4,9)
print(s)

