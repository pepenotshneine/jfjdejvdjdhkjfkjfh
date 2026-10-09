def powers_of_three(n):
    for i in range(n):
        yield 3 ** i

for number in powers_of_three(10):
    print(number)