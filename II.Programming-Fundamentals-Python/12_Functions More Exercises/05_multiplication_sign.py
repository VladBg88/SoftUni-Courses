def multiplication_sign(num1, num2, num3):
    # Check if any number is zero
    if num1 == 0 or num2 == 0 or num3 == 0:
        print("zero")
        return

    # Count the number of negative numbers
    negative_count = 0
    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1

    # Determine the sign based on the count of negative numbers
    if negative_count % 2 == 0:
        print("positive")
    else:
        print("negative")


# Example usage
user_num1 = int(input())
user_num2 = int(input())
user_num3 = int(input())
multiplication_sign(user_num1, user_num2, user_num3)
