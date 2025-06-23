def is_odd(number):
    return abs(number) % 2 != 0

for i in range(1, 11):
    print(f'Is {i} odd? {is_odd(i)}')
