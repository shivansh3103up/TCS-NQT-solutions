N = int(input("Enter the capacity of jar:"))   #10
K = 5 #minimum number of candies in jar
M = int(input("How much candies do you want:"))
if(M >= N or M == 0):
    print("INVALID INPUT")
else:
    print("Number of candies sold:",M)
    A = N-M
    print("Number of candies remaining:",A)
if (A < K):
    A = N
print("Updated value in jar",A)
