x = int(input())
y = int(input())
while x >= y :
    x = int(input())
    y = int(input())
# print(x,y)
count = 0
while x != y:
    z = y
    while x < z :
        z = z/2
    if x < z+1 :
        x *= 2
    else:
        x -= 1
    count += 1

print(count)
