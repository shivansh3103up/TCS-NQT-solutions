N = int(input("Enter the value of N: "))
balloons = []
for _ in range(N):
    x = input("Enter the colour of balloons:")
    balloons.append(x)
color_count = {} 
for balloon in balloons:
    balloon = balloon.lower()
    if balloon in color_count:
        color_count[balloon] += 1
    else:
        color_count[balloon] = 1
odd_color = "All are even"
for color, count in color_count.items():
    if count % 2 == 1:
        odd_color = color
        break
print(odd_color)
