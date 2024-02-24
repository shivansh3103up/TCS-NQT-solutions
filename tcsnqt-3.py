N = int(input("Enter the lenght of an array(N<20):"))
a = []
count = 1
for i in range(N):
    x = int(input("Enter the value of element:"))
    a.append(x)
max_element = a[0]
for i in range(1, len(a)):
    if a[i] > max_element:
        count += 1
        max_element = a[i]
print(count)