V = int(input("Enter the number of vehicles:"))
W = int(input("Enter the number of wheels:"))
if not (2 <= W and W % 2 == 0 and V < W):
    print("INVALID INPUT")
else:
    TW = ((V*4)-W)//2
    FW = V - TW
print("TW:",TW,"FW:",FW)