# ý tưởng:
# cách nhanh nhất để x => 2x thì là x*=2
"""cách nhanh nhất để x => 2x+1 thì là 2x+1 = 2*(x+1)-1
    thì để tìm x+1 ta kết hợp x*=2 và x-=1
 """
x = int(input()) # x = 3
y = int(input()) # y = 7
# thực hiện vòng lặp để luôn luôn có x < y
while x >= y :
    x = int(input())
    y = int(input())
# print(x,y)
count = 0
# thực hiện vòng lặp để có x = y
while x != y:
    z = y   # z = y = 7
    while x < z :   #1 lần 1 : x=3<z=7   # z mới = 3.5
        z = z/2     #2 lần 2 : x=3<z=3.5  # z mới = 1.75
    if x < z+1 :    #3 lần 3 : x=3>z=1.75 # thoat vong lap
        x *= 2      # x = 3 > 1.75+1 => x = x-1 = 2 => count = 1
    else:           # x = 2 < y = 7 nên quay về vòng lặp ban đầu
        x -= 1      #1,#2,#3
    count += 1      # x = 2 < 1.75+1 => x = x*2 = 4 => count = 2
print(count)        # x = 4 < y = 7 nên quay về vòng lặp ban đầu
                    #1,#2
                    # x = 4 < 3.5+1 => x = x*2 = 8 => count = 3
                    # x = 8 > y = 7 => x = x-1 = 8-1 =7 =y => count = 4
                    # in ra kết quả bằng 4
