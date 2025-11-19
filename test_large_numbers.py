from format_rubles_russian import format_rubles_russian

print("Testing larger values:")
test_values = [1000.00, 2000.00, 5000.00, 10000.00, 15000.00, 20000.00, 100000.00, 500000.00, 1000000.00]

for value in test_values:
    formatted = format_rubles_russian(value)
    print(f'{value} -> {formatted}')

print("\nTesting values with zero kopecks (should show 'ровно'):")
zero_kopeck_values = [1.00, 5.00, 10.00, 21.00, 100.00, 1000.00, 5000.00, 10000.00]
for value in zero_kopeck_values:
    formatted = format_rubles_russian(value)
    print(f'{value} -> {formatted}')