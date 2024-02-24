S = input("Enter a string consisting * , #:")
x = 0
y = 0
for i in S:
    if(i == "*"):
        x = x + 1
    elif(i == "#"):
        y = y + 1
if(x > y):
    print("Positive Integer")
elif(x < y):
    print("Negative Integer")
else:
    print("0") 