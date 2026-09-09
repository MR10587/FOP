height1 = int(input("Enter first student's height: "))
height2 = int(input("Enter second student's height: "))
height3 = int(input("Enter third student's height: "))
height4 = int(input("Enter fourth student's height: "))
height5 = int(input("Enter fifth student's height: "))

avg_height = float((height1 + height2 + height3 + height4 + height5) / 5)

taller_than_180 = 0
smaller_than_164 = 0

if (height1 > 180):
    taller_than_180 += 1
elif (height1 < 164):
    smaller_than_164 += 1  

if (height2 > 180):
    taller_than_180 += 1
elif (height2 < 164):
    smaller_than_164 += 1
    
if (height3 > 180):
    taller_than_180 += 1
elif (height3 < 164):
    smaller_than_164 += 1
    
if (height4 > 180):
    taller_than_180 += 1
elif (height4 < 164):
    smaller_than_164 += 1
    
if (height5 > 180):
    taller_than_180 += 1
elif (height5 < 164):
    smaller_than_164 += 1
    
print(f"Students taller than 180: {taller_than_180}, students smaller than 164: {smaller_than_164}, average height of students: {avg_height} ")
