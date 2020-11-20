x = int(input())
y = int(input())
while x >= y :
    x = int(input())
    y = int(input())
# print(x,y)
count = 0
# a = y//213
# a1 = a+1
# b = y//3
# c = y//4
# while x != y:
#         if x < c:
#             x *= 2
#             count += 1
#         elif c <= x < b:
#             x -= 1
#             count += 1
#         elif b <= x <= (a+1):
#             x *= 2
#             count += 1
#         else:
#             x -= 1
#             count += 1
# print(count)
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
