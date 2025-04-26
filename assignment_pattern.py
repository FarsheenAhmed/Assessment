def generate_pattern():
    for first_digit in range(1, 6):
        for last_digit in range(1, 6):
            if last_digit == first_digit + 1:
                if first_digit == 1:
                    middle_digit = str(first_digit) * 4
                elif first_digit == 3:
                    middle_digit="3"*3+"4"
                else:
                    middle_digit = str(first_digit) * 4
                pattern = str(first_digit) * 4 + middle_digit + str(last_digit)
                print(pattern)

generate_pattern()
