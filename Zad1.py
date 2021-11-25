def numbers(n):
    if n < 0:
        return
    print(f'n: {n}')
    numbers(n - 1)

numbers(10)