a = [7, 8, 6, 9, 5]
k = int(input("Enter the value: "))
k = k % len(a)

for i in range(k):
    temp = a[-1]
    for i in range(len(a) - 1, 0):
        a[i] = a[i - 1]
    a[0] = temp
print(a)
