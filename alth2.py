# ý tưởng:
# cách nhanh nhất để x => 2x thì là x*=2
"""cách nhanh nhất để x => 2x+1 thì là 2x+1 = 2*(x+1)-1
    thì để tìm x+1 ta kết hợp x*=2 và x-=1
 """
x = int(input())
y = int(input())
# thực hiện vòng lặp để luôn luôn có x < y
while x >= y :
    x = int(input())
    y = int(input())
# print(x,y)
# khởi tạo biến đếm số bước
count = 0
# thực hiện vòng lặp để có x = y
while x != y:
# gắn biến z = y để y không bao giờ thay đổi
    z = y
#so sánh x với các khoảng x/2, x/4, x/8 ,...
# thực hiện vòng lặp để biến z = z/2 để tìm được khoảng của x
    while x < z :
        z = z/2
    if x < z+1 :
        x *= 2
    else:
        x -= 1
    count += 1

print(count)
