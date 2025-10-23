numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_count = 0
odd_count = 0
prime_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        else:
            prime_count += 1


print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Prime numbers:", prime_count)

