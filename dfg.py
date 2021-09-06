#Hexadecimal to decimal program; by Kevin Liu

def getdecdigit(digit):
    digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    for i in range(len(digits)):
        if digit ==digits[i]:
            return i

def hextodec(hexnum):
    decnum = 0
    power = 0
    for digit in range(len(hexnum), 0, -1):
        decnum = decnum + 16 ** power * getdecdigit(hexnum[digit-1])
        power = power + 1
    print(str(decnum))

#Could be any number; just put in simple
#conversion = str(input())
hextodec("A5")