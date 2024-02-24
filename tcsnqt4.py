""" T = int(input("Enter the value of T: "))
E = []
for i in range(T):
    x = int(input("Enter the value of element:"))
    E.append(x)
L = []
for i in range(T):
    x = int(input("Enter the value of element:"))
    L.append(x) """
T = 5
E = [7,2,5,1,3]
L = [1,2,1,3,4]
max_guests = 0
current_guests = 0
for i in range(T):
    current_guests = current_guests + E[i] - L[i]
    if current_guests > max_guests:
        max_guests = current_guests
print(max_guests)