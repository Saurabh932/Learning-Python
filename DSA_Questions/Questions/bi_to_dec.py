# n = "101"
# sum = 0
# n_len = len(n)

# for i in range(n_len):
#     idx = int(n[i])
#     power = (n_len - 1) - i
#     sum += idx * (2**power)
    
# print(sum)


def remainder(num):
    return num//2

def mod(num):
    return num%2

num = 4
binary = ""
while num>0:
    modu = mod(num)
    rem = remainder(num)

    binary += str(modu)
    num=rem


print(binary[::-1])