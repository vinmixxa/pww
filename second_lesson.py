def sum_even_digits(num):
    sum = 0
    while num > 0:
        if num % 2 == 0:
            s = num % 10
            sum += s
        num = num // 10
    return sum

n = int(input())
a = sum_even_digits(n)
print(a)

