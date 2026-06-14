num = int(input('Enter a numbers:'))
count = 0
if num < 0:
    num =  -num
if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num =num // 10
print('The answer is:', count)

    