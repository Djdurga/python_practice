def count(num):
    count = 0
    if num == 0:
        return 1
    while num != 0:
        num = num // 10
        count += 1
    return count
num = int(input("Enter a number:"))
print(count(num))
