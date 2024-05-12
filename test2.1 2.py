h = int(input("ความสูง"))
w = int(input("ความยาวฐาน"))
if h >= 0 and w >= 0 :
    a = 1/2*h*w
    print(a)
else :
    print("ไม่สามารถคำนวณพื้นที่ได้ เพราะมีตัวเลขติดลบ")