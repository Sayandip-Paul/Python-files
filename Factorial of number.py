num = int(input("Enter a number: "))
l = []
mul = 1
while num > 0:
    l.append(num)
    num = num - 1

for item in l:
    mul = mul + item
else:
    print("The factorial is ",mul)
