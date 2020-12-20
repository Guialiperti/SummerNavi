max_value = 5000000
min_value = 1
counter = 0

for n in range(min_value, max_value + 1):
    div1 = n % 2
    div2 = n % 37
    div3 = n % 49
    if div1 == 0 and div2 == 0 and div3 == 0:
        counter += 1

print(counter)