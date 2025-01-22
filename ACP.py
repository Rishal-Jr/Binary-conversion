
n = int(input("Enter a decimal number: "))
if n == 0:
    binary = "0"
else:
    binary = ""
    power = 0
    
    while 2 ** power <= n:
        power += 1
    
    for i in range(power - 1, -1, -1):
        if n >= 2 ** i:
            binary += "1"
            n -= 2 ** i
        else:
            binary += "0"
    
print(f"The binary representation of {n} is {binary}")


