hex = (1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F")

num = int(input("Please Input a number smaller than 255:"))
# max number is 256


remainder1 = num%16
var1 = num//16
remainder2 = var1%16
var2 = var1//16
remainder3 = var2 % 16
var3 = var2//16
remainder4 = var3 %16
var4 = var3//16
remainder5 = var4 %16
var5 = var4//16
remainder6 = var5 %16
var6 = var5//16
remainder7 = var6 %16

ans1 = (hex[remainder7-1])
ans2 = (hex[remainder6-1])
ans3 = (hex[remainder5-1])
ans4 = (hex[remainder4-1])
ans5 = (hex[remainder3-1])
ans6 = (hex[remainder2-1])
ans7 = (hex[remainder1-1])





#ans1 = (hex[remainder3-1])
#ans2 = (hex[remainder2-1])
#ans3 = (hex[remainder1-1])

if num < 15:
    print (ans3)

else:
    print(ans2, ans3)
