r = 3
c = 3
rxc = [0, 1, 0, 1, 1, 0, 1, 1, 1]
max_row = 0
max_ones = 0
for i in range(0, len(rxc), c):
    row_count = 0
    for j in range(i, i + c):
        row_count += rxc[j]
    if row_count > max_ones:
        max_ones = row_count
        max_row = i / c  
print("Maximum ones:", max_ones)
print("Row with maximum ones:", max_row)
        