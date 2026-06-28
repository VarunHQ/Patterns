# ================================
# DISARIUM NUMBER CHECKER
# ================================
# A disarium number is a number where the sum of its digits 
# powered with their respective position is equal to the number.
# Example: 135 = 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

def get_number_from_user():
    """Get a positive integer from the user"""
    while True:
        try:
            num = int(input("Enter a positive number: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculate_disarium_sum(num):
    """Calculate the sum of digits powered with their respective position"""
    num_str = str(num)
    disarium_sum = 0
    
    for position, digit in enumerate(num_str, start=1):
        digit_int = int(digit)
        disarium_sum += digit_int ** position
    
    return disarium_sum


def is_disarium_number(num):
    """Check if a number is a disarium number"""
    disarium_sum = calculate_disarium_sum(num)
    return num == disarium_sum


def display_calculation(num):
    """Display the detailed calculation"""
    num_str = str(num)
    calculation = " + ".join([f"{digit}^{pos}" for pos, digit in enumerate(num_str, start=1)])
    
    result_parts = []
    for position, digit in enumerate(num_str, start=1):
        digit_int = int(digit)
        result_parts.append(f"{digit_int}^{position} = {digit_int ** position}")
    
    print(f"\nCalculation: {calculation}")
    print("Breakdown:")
    for part in result_parts:
        print(f"  {part}")
    print(f"Sum = {calculate_disarium_sum(num)}")


def main():
    """Main program"""
    print("=" * 40)
    print("DISARIUM NUMBER CHECKER")
    print("=" * 40)
    
    number = get_number_from_user()
    
    display_calculation(number)
    
    if is_disarium_number(number):
        print(f"\n✓ {number} IS a disarium number!")
    else:
        print(f"\n✗ {number} is NOT a disarium number.")
    
    print("=" * 40)


# Run the program
if __name__ == "__main__":
    main()
