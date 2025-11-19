def format_rubles_russian(total_cost):
    """
    Format a monetary amount in rubles and kopecks in Russian words.
    
    Args:
        total_cost (float): The amount in rubles (e.g., 125.75)
        
    Returns:
        str: The amount formatted in Russian words (e.g., "сто двадцать пять рублей семьдесят пять копеек")
    """
    # Convert to kopecks to avoid floating point issues
    cents = round(total_cost * 100)
    rubles = cents // 100
    kopecks = cents % 100
    
    # Russian words for numbers
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 
             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 
           'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 
               'семьсот', 'восемьсот', 'девятьсот']
    
    # Additional forms for 1, 2, and 3 in different positions (feminine forms)
    ones_feminine = ['', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    
    # Thousands groups with their forms
    thousands_groups = [
        ('', '', ''),  # hundreds (no special name)
        ('тысяча', 'тысячи', 'тысяч'),  # thousands
        ('миллион', 'миллиона', 'миллионов'),  # millions
        ('миллиард', 'миллиарда', 'миллиардов'),  # billions
    ]
    
    def number_to_russian_words(num, feminine=False):
        """Convert a number to Russian words."""
        if num == 0:
            return 'ноль'
            
        result = ''
        
        # Handle thousands groups (thousands, millions, billions)
        group_index = 0
        parts = []
        
        while num > 0:
            group = num % 1000
            num //= 1000
            
            if group > 0:
                group_words = ''
                
                # Handle hundreds
                hundreds_part = group // 100
                remainder = group % 100
                
                if hundreds_part > 0:
                    group_words += hundreds[hundreds_part] + ' '
                
                # Handle tens and teens
                if remainder >= 20:
                    tens_part = remainder // 10
                    ones_part = remainder % 10
                    group_words += tens[tens_part] + ' '
                    if ones_part > 0:
                        # Use feminine forms when requested or for thousands group
                        if (feminine or group_index == 1) and ones_part <= 4:  # thousands use feminine forms
                            group_words += ones_feminine[ones_part] + ' '
                        else:
                            group_words += ones[ones_part] + ' '
                elif remainder >= 10:
                    group_words += teens[remainder - 10] + ' '
                elif remainder > 0:
                    # Use feminine forms when requested or for thousands group
                    if (feminine or group_index == 1) and remainder <= 4:  # thousands use feminine forms
                        group_words += ones_feminine[remainder] + ' '
                    else:
                        group_words += ones[remainder] + ' '
                
                # Add thousands group name
                if group_index > 0:
                    # Determine form of thousands group
                    last_digit = group % 10
                    last_two_digits = group % 100
                    
                    if 11 <= last_two_digits <= 14:
                        group_form = thousands_groups[group_index][2]  # plural
                    elif last_digit == 1:
                        group_form = thousands_groups[group_index][0]  # singular
                    elif 2 <= last_digit <= 4:
                        group_form = thousands_groups[group_index][1]  # few
                    else:
                        group_form = thousands_groups[group_index][2]  # plural
                    
                    group_words = group_words.strip()
                    if group_words:
                        parts.append(group_words + ' ' + group_form)
                else:
                    # For hundreds group, just add the words
                    if group_words.strip():
                        parts.append(group_words.strip())
            
            group_index += 1
        
        # Combine parts in reverse order
        result = ' '.join(reversed(parts))
        return result.strip()
    
    # Format rubles
    if rubles == 0:
        rubles_words = 'ноль'
        ruble_form = 'рублей'
    else:
        rubles_words = number_to_russian_words(rubles, feminine=False)
        
        # Determine correct form of 'рубль' based on the last digit of rubles
        last_digit = rubles % 10
        last_two_digits = rubles % 100
        
        if 11 <= last_two_digits <= 14:
            ruble_form = 'рублей'
        elif last_digit == 1:
            ruble_form = 'рубль'
        elif 2 <= last_digit <= 4:
            ruble_form = 'рубля'
        else:
            ruble_form = 'рублей'
    
    # Format kopecks
    if kopecks == 0:
        # Use "ровно" instead of "ноль копеек"
        return f'{rubles_words} {ruble_form} ровно'
    else:
        # Use feminine forms for kopecks
        kopecks_words = number_to_russian_words(kopecks, feminine=True)
        
        # Determine correct form of 'копейка'
        kopecks_last_digit = kopecks % 10
        kopecks_last_two_digits = kopecks % 100
        
        if 11 <= kopecks_last_two_digits <= 14:
            kopeck_form = 'копеек'
        elif kopecks_last_digit == 1:
            kopeck_form = 'копейка'
        elif 2 <= kopecks_last_digit <= 4:
            kopeck_form = 'копейки'
        else:
            kopeck_form = 'копеек'
        
        return f'{rubles_words} {ruble_form} {kopecks_words} {kopeck_form}'


# Test the function
if __name__ == "__main__":
    # Test with example values including the specific case
    test_values = [125.75, 1.01, 2.02, 5.05, 0.01, 0.10, 11.12, 21.00, 100.00, 
                   1000.50, 1500.25, 21000.00, 1000000.00, 1234567.89, 5000.00, 2000.00, 1000.00]
    
    print("Example formatting:")
    for value in test_values:
        formatted = format_rubles_russian(value)
        print(f"{value} -> {formatted}")
        
    print("\nCorrected examples with proper gender agreement:")
    corrected_examples = [
        (1000.50, "одна тысяча рублей пятьдесят копеек"),
        (1500.25, "одна тысяча пятьсот рублей двадцать пять копеек"),
        (21000.00, "двадцать одна тысяча рублей ровно"),
        (2000.00, "две тысячи рублей ровно"),
        (3000.00, "три тысячи рублей ровно"),
        (4000.00, "четыре тысячи рублей ровно")
    ]
    
    for value, expected in corrected_examples:
        formatted = format_rubles_russian(value)
        status = "✓" if formatted == expected else "✗"
        print(f"{value} -> {formatted} {status}")