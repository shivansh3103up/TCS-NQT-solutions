num_interior_walls = int(input("Enter the number of interior walls: "))
num_exterior_walls = int(input("Enter the number of exterior walls: "))
interior_cost_per_sqft = 18
exterior_cost_per_sqft = 12
total_interior_cost = 0
total_exterior_cost = 0
for i in range(num_interior_walls):
    area = float(input("Enter the surface area of interior wall in square feet: "))
    total_interior_cost = total_interior_cost + area * interior_cost_per_sqft
for i in range(num_exterior_walls):
    area = float(input("Enter the surface area of exterior wall in square feet: "))
    total_exterior_cost = total_exterior_cost + area * exterior_cost_per_sqft
total_cost = total_interior_cost + total_exterior_cost
print("Total Cost of Painting the Property: Rs:",total_cost)
