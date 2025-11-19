from format_rubles_russian import format_rubles_russian

test_values = [1000.00, 2000.00, 3000.00, 4000.00, 5000.00, 10000.00, 21000.00, 1000000.00]

print("Testing thousands with correct feminine forms:")
for value in test_values:
    formatted = format_rubles_russian(value)
    print(f'{value} -> {formatted}')