#Kaleb Soule Lab 2


#First Question
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
result1 = 1

i = 0
while i < len(part1):
    result1 = result1 * part1[i]
    i = i + 1


for i in part1: 
    result1 = result1 * i


print('Result of First Question is:', result1)

#Second Question
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
result2 = 0

for i in part2: 
    result2 = result2 + i

print('Result of Second Question is:', result2)

#Third Question
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
result3 = 0

for i in part3:
    if i % 2 == 0:
        result3 = result3 + i
    
print('Result of Third Question is:', result3)

