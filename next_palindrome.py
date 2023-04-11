def nextPali(num):
    if str(num) == str(num)[::-1]:
        return num
    else:
        while str(num) != str(num)[::-1]:
            d = sum(map(int,str(num)))
            num = num + d
        return num

n = 69
res = nextPali(n)
print("The next palindrome is: ",res)
        
        
