n = int(input())

isPrime = True
for i in range(2, n):
    if n % i == 0 or n == 2:
        isPrime = False

print('PRIME' if isPrime else 'NOTPRIME')
