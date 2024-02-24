def remaining_monkeys(n, m, p, k, j):
    
    

n = int(input("Enter total number of Monkeys: "))
m = int(input("Enter total number of Bananas: "))
p = int(input("Enter total number of Peanuts: "))
k = int(input("Enter number of eatable Bananas by a single Monkey: "))
j = int(input("Enter number of eatable Peanuts by a single Monkey: "))

result = remaining_monkeys(n, m, p, k, j)
print("number of monkey left on tree are:", result)

