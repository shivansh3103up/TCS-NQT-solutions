a = [7,8,6,9,5]
k = int(input("enter the value:"))
k = k % len(a)
for i in range(k):
    temp = a[0]
    for i in range(1,len(a)):
        temp1 = a[i]
        a[i] = temp
        temp = temp1
    a[0] = temp1
print(a)

    