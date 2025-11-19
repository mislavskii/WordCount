from format_rubles_russian import format_rubles_russian

test_values = [1.01, 2.02, 3.03, 4.04, 5.05, 11.11, 12.12, 21.00]

print("Testing specific cases:")
for value in test_values:
    formatted = format_rubles_russian(value)
    print(f'{value} -> {formatted}')